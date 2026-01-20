from rest_framework import generics, status, serializers
from rest_framework.response import Response
from .serializers import UserDetailSerializer, DepositSerializer, WithdrawalSerializer, DepositAccountDetailsSerializer
from tables.models import UserDetail, Deposit, withdrawal, DepositAccountDetails
from decimal import Decimal
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView

# =========================
# USER AUTHENTICATION
# =========================

class UserRegistrationView(generics.CreateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        # Securely hash the password before saving
        if 'Password' in data:
            data['Password'] = make_password(data['Password'])
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserDetailSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('Email')
        password = request.data.get('Password')

        if not email or not password:
            return Response({"error": "Please provide both email and password"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserDetail.objects.get(Email=email)
            # Use check_password to verify the hashed string
            if check_password(password, user.Password):
                return Response({
                    "message": "Login successful", 
                    "user_id": user.id, 
                    "name": user.Name
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except UserDetail.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UserProfileView(generics.RetrieveAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer

    def get_object(self):
        user_id = self.kwargs.get('pk')
        password = self.request.query_params.get('password')

        if not user_id or not password:
            raise serializers.ValidationError("User ID and password are required.")

        try:
            user = UserDetail.objects.get(pk=user_id)
        except UserDetail.DoesNotExist:
            raise serializers.ValidationError("User not found.")

        # Secure verification for profile viewing
        if not check_password(password, user.Password):
            raise serializers.ValidationError("Invalid password.")

        return user

# =========================
# FINANCIAL OVERVIEW
# =========================

class UserBalanceView(APIView):
    """Provides a quick check of available trading margin."""
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        password = request.data.get('password')

        if not user_id or not password:
            return Response({"error": "User ID and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserDetail.objects.get(pk=user_id)
            if check_password(password, user.Password):
                return Response({
                    "name": user.Name,
                    "account_balance": user.Account_Balance
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except UserDetail.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class AccountSummaryView(APIView):
    """Returns balance plus the 5 most recent deposits and withdrawals."""
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        password = request.data.get('password')

        try:
            user = UserDetail.objects.get(pk=user_id)
            if not check_password(password, user.Password):
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            
            recent_deposits = Deposit.objects.filter(user=user).order_by('-id')[:5]
            recent_withdrawals = withdrawal.objects.filter(user=user).order_by('-id')[:5]

            return Response({
                "account_balance": user.Account_Balance,
                "recent_deposits": DepositSerializer(recent_deposits, many=True).data,
                "recent_withdrawals": WithdrawalSerializer(recent_withdrawals, many=True).data
            }, status=status.HTTP_200_OK)

        except UserDetail.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

# =========================
# DEPOSITS & WITHDRAWALS
# =========================

class DepositCreateView(generics.CreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

class WithdrawalCreateView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        password = request.data.get('password')
        amount = request.data.get('Amount')

        if not user_id or not password:
            return Response({"message": "Id and Password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserDetail.objects.get(id=user_id)
            
            if not check_password(password, user.Password):
                return Response({"message": "Invalid password."}, status=status.HTTP_400_BAD_REQUEST)
            
            withdrawal_amount = Decimal(amount)

            if withdrawal_amount <= 0:
                return Response({"message": "Invalid withdrawal amount."}, status=status.HTTP_400_BAD_REQUEST)

            if float(withdrawal_amount) > user.Account_Balance:
                return Response({"message": "Insufficient balance."}, status=status.HTTP_400_BAD_REQUEST)
            
            withdrawal_obj = withdrawal.objects.create(
                user=user,
                Name=user.Name,
                Amount=str(withdrawal_amount),
                Status='pending'
            )

            serializer = WithdrawalSerializer(withdrawal_obj)
            return Response({
                "message": "Withdrawal request placed successfully. Funds will be distributed within 2 business days.", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        except UserDetail.DoesNotExist:
            return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# =========================
# ACCOUNT MANAGEMENT
# =========================

class UserBankDetailsUpdateView(generics.UpdateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        password = request.data.get('Password')

        if not user_id or not password:
            return Response({"error": "User ID and password are required for authentication."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserDetail.objects.get(pk=user_id)
        except UserDetail.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if not check_password(password, user.Password):
            return Response({"error": "Invalid password."}, status=status.HTTP_401_UNAUTHORIZED)

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class DepositAccountDetailsView(generics.RetrieveAPIView):
    queryset = DepositAccountDetails.objects.all()
    serializer_class = DepositAccountDetailsSerializer

    def get_object(self):
        return DepositAccountDetails.objects.first()

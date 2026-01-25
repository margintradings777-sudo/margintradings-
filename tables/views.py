from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class UserRegistrationView(APIView):
    def post(self, request):
        data = request.data

        name = data.get("Name")
        email = data.get("Email")
        password = data.get("Password")
        phone = data.get("Phone")
        pan = data.get("Pan")
        account = data.get("Account_No")
        ifsc = data.get("IFSC_code")

        if not all([name, email, password]):
            return Response({"message": "Missing fields"}, status=400)

        if User.objects.filter(email=email).exists():
            return Response({"message": "Email already exists"}, status=400)

        user = User.objects.create_user(
            username=name,
            email=email,
            password=password
        )

        return Response({
            "message": "User created",
            "user_id": user.id,
            "phone": phone,
            "pan": pan,
            "account": account,
            "ifsc": ifsc,
        }, status=201)

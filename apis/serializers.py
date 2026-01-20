from rest_framework import serializers
from tables.models import UserDetail, Deposit, withdrawal, DepositAccountDetails
from decimal import Decimal

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'
        # This prevents the password from being leaked in GET requests
        extra_kwargs = {
            'Password': {'write_only': True}
        }

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = withdrawal
        fields = ['id', 'Name', 'Amount', 'Status', 'user']

class DepositAccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositAccountDetails
        fields = '__all__'
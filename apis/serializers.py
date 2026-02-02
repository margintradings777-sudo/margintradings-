from rest_framework import serializers
from tables.models import UserDetail, Deposit, withdrawal, DepositAccountDetails


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = "__all__"


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = "__all__"


class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = withdrawal
        fields = "__all__"


class DepositAccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositAccountDetails
        fields = "__all__"

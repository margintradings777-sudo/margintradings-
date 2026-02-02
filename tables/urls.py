from django.urls import path

from .views import (
    login_view,
    register_view,
    profile_view,
    withdrawal_view,
)

from apis.views import DepositAccountDetailsView

urlpatterns = [
    path("login/", login_view),
    path("register/", register_view),
    path("profile/<int:user_id>/", profile_view),
    path("withdrawal/", withdrawal_view),

    path("deposit-account-details/", DepositAccountDetailsView.as_view(), name="deposit_account_details"),
]


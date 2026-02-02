from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    DepositCreateView,
    WithdrawalCreateView,
    UserBankDetailsUpdateView,
    DepositAccountDetailsView,
    UserBalanceView,
    AccountSummaryView,
)

urlpatterns = [
    # Auth
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),

    # User profile & bank details
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
    path(
        "profile/<int:pk>/update-bank-details/",
        UserBankDetailsUpdateView.as_view(),
        name="update-bank-details",
    ),

    # Finance
    path("deposit/", DepositCreateView.as_view(), name="deposit"),
    path("withdrawal/", WithdrawalCreateView.as_view(), name="withdrawal"),

    path("balance/", UserBalanceView.as_view(), name="balance"),
    path("summary/", AccountSummaryView.as_view(), name="summary"),

    # Deposit account info (QR / IFSC / Bank)
    path(
        "deposit-account-details/",
        DepositAccountDetailsView.as_view(),
        name="deposit-account-details",
    ),
]

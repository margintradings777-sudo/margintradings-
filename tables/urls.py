from django.urls import path
from .views import profile_view

from apis.views import (
    UserRegistrationView,
    UserLoginView,
    WithdrawalCreateView,
    DepositAccountDetailsView,
)

urlpatterns = [
    # Auth
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),

    # Profile (tables app)
    path("profile/<int:user_id>/", profile_view, name="profile"),

    # Withdraw
    path("withdrawal/", WithdrawalCreateView.as_view(), name="withdrawal"),

    # Deposit account details
    path("deposit-account-details/", DepositAccountDetailsView.as_view(), name="deposit_account_details"),
]

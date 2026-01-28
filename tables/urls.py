from django.urls import path
from .views import (
    login_view,
    register_view,
    profile_view,
    withdrawal_view,
    deposit_account_details_view
)

urlpatterns = [
    path("login/", login_view),
    path("register/", register_view),
    path("profile/<int:user_id>/", profile_view),
    path("withdrawal/", withdrawal_view),

    
    path("deposit-account-details/", deposit_account_details_view),
]

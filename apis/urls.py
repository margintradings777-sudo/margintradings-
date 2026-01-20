from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, DepositCreateView, WithdrawalCreateView, UserBankDetailsUpdateView, DepositAccountDetailsView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('deposit/', DepositCreateView.as_view(), name='deposit-create'),
    path('withdrawal/', WithdrawalCreateView.as_view(), name='withdrawal-create'),
    path('profile/<int:pk>/update-bank-details/', UserBankDetailsUpdateView.as_view(), name='user-bank-details-update'),
    path('deposit-account-details/', DepositAccountDetailsView.as_view(), name='deposit-account-details'),
]
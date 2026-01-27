from django.urls import path
from .views import login_view, register_view, profile_view, withdrawal_view

urlpatterns = [
    path("login/", login_view),
    path("register/", register_view),
    path("profile/<int:user_id>/", profile_view),
    path("withdrawal/", withdrawal_view),
]

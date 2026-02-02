from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import UserDetail
import json


@csrf_exempt
def withdrawal_view(request):
    return JsonResponse({"message": "withdrawal endpoint placeholder"})

@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST method required"}, status=405)

    data = json.loads(request.body)
    email = data.get("Email")
    password = data.get("Password")

    try:
        user = User.objects.get(email=email)
        if not user.check_password(password):
            raise User.DoesNotExist
    except User.DoesNotExist:
        return JsonResponse({"message": "Invalid credentials"}, status=401)

    return JsonResponse({
        "user_id": user.id,
        "name": user.username,
        "email": user.email,
    })


@csrf_exempt
def register_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST method required"}, status=405)

    name = request.POST.get("Name")
    email = request.POST.get("Email")
    password = request.POST.get("Password")

    if User.objects.filter(email=email).exists():
        return JsonResponse({"message": "Email already exists"}, status=400)

    user = User.objects.create_user(
        username=name,
        email=email,
        password=password
    )

    return JsonResponse({
        "message": "User created",
        "user_id": user.id
    })


def profile_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)

    return JsonResponse({
        "Name": user.username,
        "Email": user.email,
        "Phone": "",
    })

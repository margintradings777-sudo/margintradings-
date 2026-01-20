from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST method required"}, status=405)

    data = json.loads(request.body)

    username = data.get("username") or data.get("Username")
    password = data.get("password") or data.get("Password")

    if not username or not password:
        return JsonResponse({"message": "Username and password required"}, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"message": "Invalid username or password"}, status=401)

    return JsonResponse({
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
    })


@csrf_exempt
def register_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST method required"}, status=405)

    data = json.loads(request.body)

    username = data.get("username") or data.get("Username")
    email = data.get("email") or data.get("Email")
    password = data.get("password") or data.get("Password")

    if not username or not email or not password:
        return JsonResponse({"message": "All fields required"}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"message": "Username already exists"}, status=400)

    if User.objects.filter(email=email).exists():
        return JsonResponse({"message": "Email already exists"}, status=400)

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return JsonResponse({
        "message": "User created successfully",
        "user_id": user.id
    })


def profile_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)

        return JsonResponse({
            "Name": user.username,
            "Email": user.email,
            "Phone": "",
        })

    except User.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)

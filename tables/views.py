from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST method required"}, status=405)

    try:
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return JsonResponse(
                {"message": "Username and password required"},
                status=400
            )

        user = authenticate(username=username, password=password)

        if user is None:
            return JsonResponse(
                {"message": "Invalid username or password"},
                status=401
            )

        return JsonResponse({
            "user_id": user.id,
            "username": user.username,
        })

    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)


@csrf_exempt
def register_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST method required"}, status=405)

    try:
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return JsonResponse(
                {"message": "Username and password required"},
                status=400
            )

        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {"message": "Username already exists"},
                status=400
            )

        user = User.objects.create_user(
            username=username,
            password=password
        )

        return JsonResponse({
            "message": "User created successfully",
            "user_id": user.id
        })

    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)

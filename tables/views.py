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
        email = data.get("Email") or data.get("email")
        password = data.get("Password") or data.get("password")

        if not email or not password:
            return JsonResponse({"message": "Email and password required"}, status=400)

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            return JsonResponse({"message": "Invalid email or password"}, status=401)

        user = authenticate(username=username, password=password)

        if user is None:
            return JsonResponse({"message": "Invalid email or password"}, status=401)

        return JsonResponse({
            "user_id": user.id,
            "name": user.username,
            "email": user.email,
        })

    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)


@csrf_exempt
def register_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST method required"}, status=405)

    try:
        data = json.loads(request.body)

        name = data.get("Name")
        email = data.get("Email")
        password = data.get("Password")

        if not name or not email or not password:
            return JsonResponse({"message": "All fields required"}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"message": "Email already exists"}, status=400)

        user = User.objects.create_user(
            username=name,
            email=email,
            password=password
        )

        return JsonResponse({
            "message": "User created successfully",
            "user_id": user.id
        })

    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)
      

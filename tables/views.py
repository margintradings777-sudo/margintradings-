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

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return JsonResponse({"message": "Username & password required"}, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"message": "Invalid username or password"}, status=401)

    return JsonResponse({
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
    })


@csrf_exempt
def profile_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)

        return JsonResponse({
            "Name": user.username,
            "Email": user.email,
            "Phone": "",   # Django User me phone nahi hota
        })

    except User.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)
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

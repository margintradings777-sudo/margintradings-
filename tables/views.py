import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import UserDetail


@csrf_exempt
def register_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST method required"}, status=405)

    name = request.POST.get("Name")
    email = request.POST.get("Email")
    password = request.POST.get("Password")
    phone = request.POST.get("Phone")

    if not all([name, email, password]):
        return JsonResponse({"message": "Missing fields"}, status=400)

    if UserDetail.objects.filter(Email=email).exists():
        return JsonResponse({"message": "Email already exists"}, status=400)

    user = UserDetail.objects.create(
        Name=name,
        Email=email,
        Password=make_password(password),
        Phone=phone,
    )

    return JsonResponse({
        "message": "User created",
        "user_id": user.id
    })


@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST method required"}, status=405)

    data = json.loads(request.body)
    email = data.get("Email")
    password = data.get("Password")

    try:
        user = UserDetail.objects.get(Email=email)
    except UserDetail.DoesNotExist:
        return JsonResponse({"message": "Invalid credentials"}, status=401)

    if not check_password(password, user.Password):
        return JsonResponse({"message": "Invalid credentials"}, status=401)

    return JsonResponse({
        "user_id": user.id,
        "name": user.Name,
        "email": user.Email,
    })


def profile_view(request, user_id):
    try:
        user = UserDetail.objects.get(id=user_id)
    except UserDetail.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)

    return JsonResponse({
        "Name": user.Name,
        "Email": user.Email,
        "Phone": user.Phone,
    })

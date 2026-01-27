from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import UserDetail

@csrf_exempt
def withdrawal_view(request):
    if request.method == "GET":
        data = list(Withdrawal.objects.values())
        return JsonResponse(data, safe=False)

    if request.method == "POST":
        body = json.loads(request.body)
        Withdrawal.objects.create(**body)
        return JsonResponse({"status": "created"})

@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST method required"}, status=405)

    import json
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

    print("POST:", request.POST)
    print("FILES:", request.FILES)

    name = request.POST.get("Name")
    email = request.POST.get("Email")
    password = request.POST.get("Password")
    phone = request.POST.get("Phone")
    pan = request.POST.get("Pan")
    account = request.POST.get("Account_No")
    ifsc = request.POST.get("IFSC_code")

    if not all([name, email, password, phone, pan, account, ifsc]):
        return JsonResponse({"message": "Missing fields"}, status=400)

    if User.objects.filter(email=email).exists():
        return JsonResponse({"message": "Email already exists"}, status=400)

    user = User.objects.create_user(
        username=name,
        email=email,
        password=password
    )

    return JsonResponse({
        "message": "User created",
        "user_id": user.id,
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

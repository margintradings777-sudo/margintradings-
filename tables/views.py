from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class UserRegistrationView(APIView):
    @csrf_exempt
def register_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST method required"}, status=405)

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

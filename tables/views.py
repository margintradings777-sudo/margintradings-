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

@csrf_exempt
def register_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST method required"}, status=405)

    name = request.POST.get("Name")
    email = request.POST.get("Email")
    password = request.POST.get("Password")
    phone = request.POST.get("Phone")
    pan = request.POST.get("Pan")
    account_no = request.POST.get("Account_No")
    ifsc_code = request.POST.get("IFSC_code")

    pan_img = request.FILES.get("Pan_card_Image")
    bank_doc = request.FILES.get("Cancel_cheque_or_bank_statement")

    # basic validation
    if not all([name, email, password, phone, pan, account_no, ifsc_code, pan_img, bank_doc]):
        return JsonResponse({"message": "Missing fields"}, status=400)

    if UserDetail.objects.filter(Email=email).exists():
        return JsonResponse({"message": "Email already exists"}, status=400)

    user = UserDetail.objects.create(
        Name=name,
        Email=email,
        Password=make_password(password),   # password hash
        Phone=phone,
        Pan=pan,
        Pan_card_Image=pan_img,
        Account_No=account_no,
        IFSC_code=ifsc_code,
        Cancel_cheque_or_bank_statement=bank_doc,
    )

    return JsonResponse({"message": "User created", "user_id": user.id})


def profile_view(request, user_id):
    try:
        user = UserDetail.objects.get(id=user_id)
    except UserDetail.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)

    return JsonResponse({
        "Name": user.Name,
        "Email": user.Email,
        "Phone": user.Phone,
        "Pan": user.Pan,
        "Account_No": user.Account_No,
        "IFSC_code": user.IFSC_code,
        "Pan_card_Image": user.Pan_card_Image.url if user.Pan_card_Image else "",
        "Cancel_cheque_or_bank_statement": user.Cancel_cheque_or_bank_statement.url if user.Cancel_cheque_or_bank_statement else "",
    })

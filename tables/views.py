from django.http import JsonResponse
from .models import UserDetail

def safe_file_url(request, file_field):
    try:
        if file_field and getattr(file_field, "name", ""):
            return request.build_absolute_uri(file_field.url)
    except Exception:
        pass
    return ""

def profile_view(request, user_id):
    try:
        user = UserDetail.objects.get(id=user_id)
    except UserDetail.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)

    data = {
        "Name": getattr(user, "Name", "") or "",
        "Email": getattr(user, "Email", "") or "",
        "Phone": getattr(user, "Phone", "") or "",

        # PAN / Bank fields - yaha exact model field name hona chahiye
        "PAN_No": getattr(user, "PAN_No", "") or "",
        "Account_No": getattr(user, "Account_No", "") or "",
        "IFSC_Code": getattr(user, "IFSC_Code", "") or "",

        # Images / documents - yaha bhi model field name exact
        "PAN_Image": safe_file_url(request, getattr(user, "Pan_card_Image", None) or getattr(user, "PAN_Image", None)),
        "Bank_Statement": safe_file_url(request, getattr(user, "Cancel_cheque_or_bank_statement", None) or getattr(user, "Bank_Statement", None)),

        "Account_Balance": float(getattr(user, "Account_Balance", 0) or 0),
    }

    return JsonResponse(data, status=200)

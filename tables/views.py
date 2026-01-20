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

        if User.objects.filter(username=email).exists():
            return JsonResponse({"message": "Email already exists"}, status=400)

        user = User.objects.create_user(
            username=email,   # 🔥 EMAIL AS USERNAME
            email=email,
            password=password
        )

        return JsonResponse({
            "message": "User created successfully",
            "user_id": user.id
        })

    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)

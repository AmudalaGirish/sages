from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_http_methods
from .models import User
import json

@csrf_exempt # # Disable CSRF for testing (not recommended for production without CSRF protection)
@require_http_methods(["POST"])  # Allow only POST requests
def login(request):
    try:
        data = json.loads(request.body)
        contact = data.get("contact")
        
        # Validate if contact number is provided
        if not contact:
            return JsonResponse({"error": "Contact number is required."}, status=400)

        # Fetch the user from the database
        user = User.objects.filter(contact=contact).first()

        if user:
            # Respond with user details
            return JsonResponse({
                "success": True,
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "contact": user.contact,
                    "address": user.address,
                    "etype": user.etype,
                    "is_admin": user.is_admin,
                }
            })
        else:
            return JsonResponse({"success": False, "message": "User not found"}, status=404)

    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)}, status=500)


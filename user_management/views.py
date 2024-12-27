from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]  # Open to everyone

    def post(self, request):
        data = request.data

        # Validation
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            return Response({"error": "Passwords do not match."}, status=HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=data.get('username')).exists():
            return Response({"error": "Username already exists."}, status=HTTP_400_BAD_REQUEST)

        if User.objects.filter(contact=data.get('contact')).exists():
            return Response({"error": "Contact number already exists."}, status=HTTP_400_BAD_REQUEST)

        # Create user
        user = User.objects.create_user(
            username=data.get('username'),
            password=password,
            contact=data.get('contact'),
            address=data.get('address'),
            role=User.CUSTOMER  # Default to 'Customer'
        )

        return Response({"success": "User registered successfully!"}, status=HTTP_200_OK)


class LoginView(APIView):
    permission_classes = [AllowAny]  # Open to everyone

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }, status=HTTP_200_OK)

        return Response({"error": "Invalid credentials."}, status=HTTP_401_UNAUTHORIZED)


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]  # Accessible only to authenticated users

    def get(self, request):
        # Sample response
        return Response({"message": f"Welcome {request.user.username}!"}, status=HTTP_200_OK)

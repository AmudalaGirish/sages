from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    CUSTOMER = 'customer'
    EMPLOYEE = 'employee'

    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (EMPLOYEE, 'Employee'),
    ]
    contact = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default=CUSTOMER,  # Default to 'customer' or any other value you prefer
    )
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

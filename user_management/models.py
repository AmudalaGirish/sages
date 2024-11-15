from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    etype = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

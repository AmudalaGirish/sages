from django.db import models
from customers.models import Customer
from user_management.models import User

class Enquiry(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    lob_id = models.CharField(max_length=50)
    site_visit = models.CharField(max_length=100)
    quotation = models.CharField(max_length=100)
    amount = models.FloatField()
    pending_amount = models.FloatField()
    status = models.CharField(max_length=50)
    po = models.CharField(max_length=50)
    material = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    remarks = models.TextField(blank=True)
    payment_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Enquiry for {self.customer.name} - {self.status}"

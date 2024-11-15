from django.db import models
from customers.models import Customer
from user_management.models import User

class Sales(models.Model):
    lob_id = models.CharField(max_length=50, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    amount = models.FloatField()
    payment_status = models.CharField(max_length=50)
    pending_amount = models.FloatField()
    sale_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sale for {self.customer.name} - {self.status}"

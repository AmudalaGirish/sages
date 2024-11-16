from django.db import models

class Invoice(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_address = models.TextField()
    invoice_number = models.CharField(max_length=50, unique=True)
    invoice_date = models.DateField(auto_now_add=True)
    po_number = models.CharField(max_length=50, blank=True, null=True)
    subtotal = models.FloatField()
    cgst = models.FloatField()
    sgst = models.FloatField()
    grand_total = models.FloatField()

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    hsn_code = models.CharField(max_length=20)
    quantity = models.IntegerField()
    rate = models.FloatField()
    amount = models.FloatField()

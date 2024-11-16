# views.py in invoice app
from django.shortcuts import render
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm, InvoiceItemForm
from django.http import HttpResponse
from num2words import num2words  # For converting amount to words
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa  # Library for PDF generation

def create_invoice(request):
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        item_forms = [InvoiceItemForm(request.POST, prefix=str(i)) for i in range(1, 11)]

        if invoice_form.is_valid() and all([form.is_valid() for form in item_forms]):
            invoice = invoice_form.save(commit=False)
            subtotal = 0

            for form in item_forms:
                item = form.save(commit=False)
                item.amount = item.quantity * item.rate
                subtotal += item.amount
                item.invoice = invoice
                item.save()

            invoice.subtotal = subtotal
            invoice.cgst = subtotal * 0.09  # 9%
            invoice.sgst = subtotal * 0.09  # 9%
            invoice.grand_total = subtotal + invoice.cgst + invoice.sgst
            invoice.save()

            return render(request, 'invoice/invoice_success.html', {'invoice': invoice})
    else:
        invoice_form = InvoiceForm()
        item_forms = [InvoiceItemForm(prefix=str(i)) for i in range(1, 11)]

    return render(request, 'invoice/create_invoice.html', {
        'invoice_form': invoice_form,
        'item_forms': item_forms,
    })

def render_pdf_view(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    template_path = 'invoice/pdf_template.html'
    context = {'invoice': invoice}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

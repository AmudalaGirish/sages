from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_invoice, name='create_invoice'),
    path('download/<int:invoice_id>/', views.render_pdf_view, name='download_invoice'),
]

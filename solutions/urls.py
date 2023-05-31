from django.urls import path
from . import views

app_name = 'solutions'   # Optional: Namespace for the app's URLs

urlpatterns = [
    path('', views.home, name='home'),
]

from django.shortcuts import render

def enquiry(request):
    return render(request, 'core/enquiry.html')

from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages
# Create your views here.

def contactme(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, f'Thank you {name}, we will get in touch with you soon.')
    return redirect('contact')




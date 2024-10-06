from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
def index(request):
    context = {
        'variable' : 'this is sent'
    }
    return render(request , 'index.html', context)
    #return HttpResponse('This is Homepage')

def about(request):
    return render(request , 'about.html')

def services(request):
    return render(request , 'service.html')

def contact(request):
    if request.method == 'POST':
        # Get the data from the form using the correct field names
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Ensure the field names match the model exactly
        contact_entry = Contact(name=name, lname=lname, phone=phone, email=email, message=message, date=datetime.today())
        contact_entry.save()  # Save the entry to the database
        messages.success(request, "Your profile was updated.")

    return render(request , 'contact.html')
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):

    if request.method == "POST":
        full_name = request.POST.get("full-name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone-number")
        message = request.POST.get("message")

        Message.objects.create(
            full_name = full_name,
            email = email,
            phone_number = phone_number,
            message = message
        )
        return redirect(index)

    return render(request, 'home1.html')   #Another way to return templates



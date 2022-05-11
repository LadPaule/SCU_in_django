from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm
from birdsong.models import Contact
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.get_or_create(email=form.cleaned_data["email"])
            form.save()
            messages.success(request, "You have been signed up!")
            return redirect("/")
    else:
        form = ContactForm()

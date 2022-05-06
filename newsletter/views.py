import json 
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.http import request
from django.conf import settings


def post(request):
    email = request.POST.get("email")
    response = redirect('/')
    data = EmailMessage(
        subject="New email newsletter subscription",
        body="You have a new email newsletter subscription, from: " + email,
        from_email= settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER],
        reply_to=[email]
    )
    data.send()
    return HttpResponseRedirect('/')
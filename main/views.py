from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method=="POST":
        Contact = Contacus()
        Contact.First_name=request.POST.get('First_name')
        Contact.Second_name=request.POST.get('Second_name')
        Contact.mobile=request.POST.get('mobile')
        Contact.email=request.POST.get('email')
        Contact.Message=request.POST.get('Message')
        Contact.save()
        return HttpResponseRedirect('/')
    image = Image.objects.all()
    return render(request,"index.html",{'image':image} )
    
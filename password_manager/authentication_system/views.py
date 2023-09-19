from django.shortcuts import render, redirect
from .models import MyUsers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UserForm
import psycopg2

# Create your views here.
def home(request):
    name = "raunak varma"
    return render(request,'authentication/index.html',{"name":name})

def new(request):
    place = "nagpur"
    return render(request,'authentication/new.html', {"place":place})

def add_user(request):
    submitted = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_user?submitted=True')
    else:
        form = UserForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'authentication/add_user.html',{'form':form,'submitted':submitted})

def show_record(request):
    data = MyUsers.objects.all()
    return render(request, 'authentication/show_record.html',{'data':data})



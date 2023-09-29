from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .modelform import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .authenticate_user import *

# Create your views here.


def home_view(request):
    if request.method =='GET':
        return render(request,'actress_app/home.html')

@authenticate_user
def signup_view(request):
    if request.method =='GET':
        frm_unbound = UserCreationForm()
        d = {'frm':frm_unbound}
        return render(request,'actress_app/signuppage.html',context=d)
    elif request.method == 'POST':
        frm_bound = UserCreationForm(request.POST)
        d = {'frm':frm_bound}
        if frm_bound.is_valid():
            u = frm_bound.save()
            u.is_staff = True
            u.save()
            return render(request,'actress_app/home.html')
        else:
            return render(request,'actress_app/signuppage.html',context=d)


def login_view(request):
    if request.method =='GET':
        return render(request,'actress_app/loginpage.html')
    elif request.method =='POST':
        u_name = request.POST.get('uname')
        u_pass = request.POST.get('upass')
        u = authenticate(request,username=u_name,password=u_pass)
        if u is not None:
            login(request,u)
            return render(request,'actress_app/home.html')
        else:
            return render(request,'actress_app/loginpage.html')


def logout_view(request):
    logout(request=request)
    return render(request,'actress_app/home.html')



@login_required(login_url='login')
def aish_view(request):
    aish = Aish.objects.all()
    d = {'aish':aish}
    return render(request,'actress_app/aish.html',context=d)

@login_required(login_url='login')
def ananya_view(request):
    ananya = Ananya.objects.all()
    d = {'ananya':ananya}
    return render(request,'actress_app/ananya.html',context=d)

@login_required(login_url='login')
def emma_view(request):
    em = Emma.objects.all()
    d = {'em':em}
    return render(request,'actress_app/emma.html',context=d)

@login_required(login_url='login')
def krish_view(request):
    krish = Krish.objects.all()
    d = {'krish':krish}
    return render(request,'actress_app/krist.html',context=d)



def add_emma_pic(request):
    if request.method =='GET':
        frm_unbound = Emma_model_form()
        d = {'frm':frm_unbound}
        return render(request,'actress_app/addemma.html',context=d)
    elif request.method == 'POST':
        frm_bound = Emma_model_form(request.POST,files=request.FILES)
        d = {'frm':frm_bound}
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("Pic Added")
        else:
            return render(request,'actress_app/addemma.html',context=d)


def add_krish_pic(request):
    if request.method =='GET':
        frm_unbound = Krish_model_form()
        d = {'frm':frm_unbound}
        return render(request,'actress_app/addkrishpic.html',context=d)
    elif request.method == 'POST':
        frm_bound = Krish_model_form(request.POST,files=request.FILES)
        d = {'frm':frm_bound}
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("Pic Added")
        else:
            return render(request,'actress_app/addkrishpic.html',context=d)



def add_aish_pic(request):
    if request.method =='GET':
        frm_unbound = Aish_model_form()
        d = {'frm':frm_unbound}
        return render(request,'actress_app/addaishpic.html',context=d)
    elif request.method == 'POST':
        frm_bound = Aish_model_form(request.POST,files=request.FILES)
        d = {'frm':frm_bound}
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("Pic Added")
        else:
            return render(request,'actress_app/addaishpic.html',context=d)




def add_ananya_pic(request):
    if request.method =='GET':
        frm_unbound = Ananya_model_form()
        d = {'frm':frm_unbound}
        return render(request,'actress_app/addananyapic.html',context=d)
    elif request.method == 'POST':
        frm_bound = Ananya_model_form(request.POST,files=request.FILES)
        d = {'frm':frm_bound}
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("Pic Added")
        else:
            return render(request,'actress_app/addananyapic.html',context=d)
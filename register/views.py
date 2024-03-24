from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from customadmin.models import Nmgmt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from register.models import Form
from django.urls import reverse

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    
    # print(FormData)

    return render (request,'homepage.html')
@login_required(login_url='login')
def FormPage(request):
    if request.method=='POST':
        name=request.POST['name']
        fname=request.POST['fname']
        contact=request.POST['contact']
        email=request.POST['email']
        dob=request.POST['dob']
        address=request.POST['address']
        idno=request.POST['idno']
        idimg=request.POST['idimg']
        rnumber=request.POST['rnumber']
        print(name,fname,contact,email,dob,address,idno,rnumber)
        form = Form(name=name,fname=fname,contact=contact,email=email,
                   dob=dob,address=address,idno=idno,idimg=idimg,rnumber=rnumber)
        form.save()
    else:
        form=Form()
    return render(request, 'form.html')

    

def SignupPage(request):
    # return render (request,'signup.html')
# def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')
def LoginPage(request):
    # def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            # login(request,user)
            # return redirect('homepage')
            if user.is_superuser:
                return HttpResponse("Superusers are not allowed to log in here,.")
            else:
                login(request, user)
                return redirect('homepage')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')
    # return render(request,'login.html')
def AboutPage(request):
    return render(request,'about.html')
def PageNotFound(request):
    return render(request,'errorpage.html')

def NoticePage(request):
    NoticeData=Nmgmt.objects.all()
    return render(request,'noticet.html',{'data':NoticeData})
def AntiRng(request):
    return render(request,'aragging.html')
def PhotosG(request):
    return render(request,'photo.html')
def LogoutPage(request):
    logout(request)
    return redirect(reverse('login'))


# table show in admin


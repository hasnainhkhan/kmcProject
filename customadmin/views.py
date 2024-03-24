from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.messages import constants as messages
from django.contrib.auth.models import User
from customadmin.models import Nmgmt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from register.models import Form
# Create your views here.

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('../admin/dashboard')
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj= User.objects.filter(username = username)
            if not user_obj.exists():
                messages.info(request,'Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            user_obj = authenticate(username= username,password = password)
            if user_obj and user_obj.is_superuser:
                login(request,user_obj)
                return redirect('../admin/dashboard')
            messages.info(request,'Invilid password')
            return redirect('/')
        return render(request,'alogin.html')
    except Exception as e:
        print(e)
def NoTice(request):
    if request.method=='POST':
        msg=request.POST.get['admsg']
        adms=Nmgmt(msg=msg)
        print(adms.msg)
        
        adms.save()
    else:
        adms=Nmgmt()

    return render(request,'notice.html')
@login_required(login_url='admin_login')
def dashboard(request):
    return render(request,'dashboard.html')
@login_required(login_url='admin_login')
def Slist(request):
    # student table data
    FormData=Form.objects.all()
    return render(request,'studentlist.html',{'data':FormData})
def NoTice(request):
    return render(request,'notice.html')

# admin logout views
def Logout_Page(request):
    logout(request)
    return redirect(reverse('admin_login'))

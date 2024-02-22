from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Customer
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from Customer.middlewares.auth import auth_middleware



def home(request):
    
    return render(request,'index.html')


def customer_home(request):
    return render(request,'home.html')

@auth_middleware
def landingpage(request):
    return render(request, 'home.html')


def login(request):
    check_loggined = request.session.get('user')
    if not check_loggined:
        if request.method == "POST":
            email = request.POST['email']
            passwords = request.POST['password']
            # user =authenticate(request,email="mac1@gmail.com",password="User@123456")
            user = authenticate(request, username=email, password=passwords)
            if user is None:
                return redirect('login')
            else:
                userInfo = Customer.objects.get(email=user)

                request.session.clear()
                request.session['user'] = userInfo.id
                request.session['user_id']=userInfo.id
                request.session['name'] = userInfo.name
                request.session['email'] = userInfo.email
                request.session['phone']=userInfo.phone
                request.session['role'] = userInfo.role

                # return render(request, 'home.html')
                return redirect('landingpage')
    else:
        return redirect('landingpage')
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')




def saves(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        confirm_password = request.POST['confirm_password']

        user = Customer(name = name,email=email,phone=phone,password=password, role=role)
        user.save()
        auth_user = User.objects.create_user(username= email,email=email,password=password)
        auth_user.save()
        
        # messages.success(request,'Your form has been submitted succcesfully')

        

    return redirect('login')


def logout(request):
    request.session.clear()
    return redirect('home')
# def show_data(request):
#     data = Package.objects.all()
#     return render(request,'register.html',{'data':data})

# def check(request):
    
#     return render(request,'check.html')

def test(request):
    return render(request, 'auth_base.html')
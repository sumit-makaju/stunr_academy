from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Package,Booking
from Customer.models import Customer
from Customer.middlewares.auth import auth_middleware
# Create your views here.
@auth_middleware
def show_data(request):
    data = Package.objects.all()
    context ={'datas':data}
    return render(request,'show_data.html',context)

def check(request,id):
    package_id = id
    trainer = Customer.objects.filter(role="trainer")
    return render(request,'check.html', {'package_id' : package_id, 'trainer': trainer} )

@auth_middleware
def checkout(request):
    advance_amount = request.POST['advance_amount']
    package_id = request.POST['package_id']
    trainer_id = request.POST['trainer']
    user_id = request.session['user_id']
    
    booking_data = Booking(user_id=user_id,trainer_id=trainer_id,package_id=package_id,advance_amount=advance_amount)
    booking_data.save()
    return redirect('my_booking')

@auth_middleware
def my_booking(request):
    user_id = request.session['user_id']
    booking_data = []
    
    data = Booking.objects.filter(user_id=user_id)
    for i in data:
        trainer = Customer.objects.get(id=i.trainer_id)
        package = Package.objects.get(id=i.package_id)
        booking_data.append([trainer.name,trainer.phone,package.package_type, package.price, i.advance_amount, package.price-i.advance_amount])
    return render(request, 'booking.html', {'data':booking_data})

@auth_middleware
def my_students(request):
    user_id = request.session['user_id']
    booking_data = []
    
    data = Booking.objects.filter(trainer_id=user_id)
    print(data)
    for i in data:
        user = Customer.objects.get(id=i.user_id)
        package = Package.objects.get(id=i.package_id)
        booking_data.append([user.name,user.phone,package.package_type, package.price, i.advance_amount, package.price-i.advance_amount])
    print(booking_data)
    return render(request,'mystudents.html', {'data': booking_data})
from django.urls import path
from Package import views


urlpatterns = [
    
    path('show/', views.show_data,name="show_data"),
    path('check/<int:id>', views.check,name="check"),
    path('check-out/', views.checkout,name="checkout"),
    path('my-bookings/', views.my_booking,name="my_booking"),
    path('my-students/', views.my_students,name="my_students"),
    # path('login/', views.login,name="login"),
    # path('register/', views.register,name="register"),
    # path('saves/', views.saves,name="saves"),
]

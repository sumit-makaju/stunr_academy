
from django.urls import path
from Customer import views
from .views import login


urlpatterns = [
    
    path('', views.customer_home,name="custome_home"),
    path('login/', views.login,name="login"),
    path('register/', views.register,name="register"),
    path('saves/', views.saves,name="saves"),
    path('home-page', views.landingpage, name="landingpage"),
    path('log-out', views.logout, name="logout"),
    # path('check/', views.check,name="check"),
    # path('show/', views.show_data,name="show_data"),
    path('test/', views.test)
]

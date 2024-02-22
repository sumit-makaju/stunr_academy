from django.urls import path
from Trainer import views

urlpatterns = [
    
    path('', views.home,name="trainer_home"),
#     path('login/', views.login,name="login"),
#     path('register/', views.register,name="register"),
#     path('saves/', views.saves,name="saves"),
# ]

]
from django.urls import path
from home import views

urlpatterns = [
    path('dashbord/',views.home , name='home'),
    path('',views.Login , name='login'),
    path('logout/',views.logoutUser , name='logout'),
    path('register/',views.Register , name='register'),
]
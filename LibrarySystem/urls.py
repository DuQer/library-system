from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.index,name='index'),
    path('staff/', views.staff, name='staff'),
    path('stafflogin/', views.stafflogin, name='stafflogin'),
    path('staffsignup/', views.staffsignup, name='staffsignup'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

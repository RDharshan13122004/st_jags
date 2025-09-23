from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'staff'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('dashboard/<slug:slug>/',views.staff_dashboard,name="staff_dashboard"),
    path('dashboard/<slug:slug>/profile/', views.staff_profile, name="staff_profile"),
    path('logout/', views.staff_logout, name='staff_logout'),
    path('login/', views.staff_login, name='staff_login'),
    path('dashboard/<slug:slug>/student_profile/<slug:student_slug>/', views.student_profile_record, name='student_profile_record'),
    path('dashboard/<slug:slug>/student_profile/<slug:student_slug>/edit/', views.edit_student_profile, name='student_edit_record'),
]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

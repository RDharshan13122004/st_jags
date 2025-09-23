from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'student'

urlpatterns = [
    #path('test/',views.test, name='test'),
    path('',views.index, name='main_index'),
    path('bba_depart/', views.bba_depart, name='bba_depart'),
    path('aero_space/',views.aero_space, name='aero_space_depart'),
    path('bca/',views.bca,name='bca_depart'),
    path('cse/',views.cse,name='cse_depart'),
    path('eee/',views.eee,name='eee_depart'),
    path('eng/',views.eng,name='eng_depart'),
    path('math/',views.math,name='math_depart'),
    path('mechanical/',views.mechanical,name='mechanical_depart'),
    path('dashboard/<slug:slug>/', views.student_dashboard, name='student_dashboard'),
    path('login/', views.student_login, name='student_login'),
    path('register/', views.student_register, name='student_register'),
    path('dashboard/<slug:slug>/profile/', views.student_profile, name='student_profile'),
    path('logout/', views.student_logout, name='student_logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
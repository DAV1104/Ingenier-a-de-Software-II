from django.urls import path
from playground.views import succesful_register
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('trainers/', views.trainers, name='trainers'),
    path('contact/', views.contact, name='contact'),
    path('course-details', views.course_details, name='course-details'),
    path('homepage/', views.homepage, name='homepage'),
    path('course-section/', views.course_section, name='course-section'),
    path('starter-page/', views.starter_page, name='starter-page'),
    path('succesful-register/', views.succesful_register, name='succesful-register')
]
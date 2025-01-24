from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('units/', views.unit_list, name='unit_list'),
    path('summary/', views.enrollments_summary, name='enrollments_summary'),
    # path('select-units/', views.unit_selection, name='unit_selection'),
    path('register/', views.student_register, name='student_register'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('doctorsearch/',views.search_view, name='doctorsearch'),
    path('doctor/<int:doctor_id>/', views.doctor_detail_view, name='doctor_detail'),
    path('specializations/', views.specializations_list, name='specializations_list'),
    path('doctors/<str:specialization>/', views.doctors_by_specialization, name='doctors_by_specialization'),
    path('area/', views.area_list, name='area_list'),
    path('doctor/<str:area>/', views.doctors_by_area, name='doctors_by_area'),

]

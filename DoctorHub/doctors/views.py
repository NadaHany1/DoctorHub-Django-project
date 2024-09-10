from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from .models import Doctor
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django import forms 

from django.db.models import Q

@login_required
def home_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/home.html', {'doctors': doctors})

def search_view(request):
    if request.method == "POST":
        specialization = request.POST.get('Specialization-input')
        area = request.POST.get('Area-input')
        if specialization == "" and area != "":
            doctors = Doctor.objects.filter(area__icontains=area)
            return render(request, 'registration/search_results.html',{'doctors': doctors})
        elif area == "" and specialization != "":
            doctors = Doctor.objects.filter(specialization__icontains=specialization)
            return render(request, 'registration/search_results.html',{'doctors': doctors})
        elif specialization == "" and area == "":
            return HttpResponse("Please Choose Area Or Specializtion Or Both")
        else:
            doctors = Doctor.objects.filter(specialization__icontains=specialization, area__icontains=area)
            specialization_doctors = Doctor.objects.filter(specialization__icontains=specialization).exclude(id__in=doctors.values('id'))
            area_doctors = Doctor.objects.filter(area__icontains=area).exclude(id__in=doctors.values('id'))
            return render(request, 'doctors/search_results.html',
            {'doctors': doctors,
            "specialization_doctors" : specialization_doctors,
            "area_doctors" : area_doctors})
    else:
        return render(request, 'doctors/home.html')

def area_list(request):
    return render(request, 'doctors/areas_list.html')

def doctors_by_area(request, area):
    doctors = Doctor.objects.filter(area__icontains=area)
    return render(request, 'doctors/areas_result.html', {'doctors': doctors, 'area':area})

def specializations_list(request):
    return render(request, 'doctors/specializations_list.html')

def doctors_by_specialization(request, specialization):
    doctors = Doctor.objects.filter(specialization__icontains=specialization)
    return render(request, 'doctors/specialization_result.html', {'doctors': doctors, 'specialization': specialization})


def doctor_detail_view(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'doctors/doctor_detailes.html', {'doctor': doctor})




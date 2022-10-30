from datetime import datetime
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from bmicalculator.models import BmiCalculator
from bmicalculator.forms import BmiCalculatorForm
from django.contrib.auth.decorators import login_required
from django.core import serializers


# Create your views here.
# @login_required(login_url='/login/')
def show_bmicalculator(request):
    form = BmiCalculatorForm()
    return render(request, "bmicalculator.html",{'form' : form, 'nama' : request.user})
   

# @login_required(login_url='/login/')
def show_json(request):
    # bmicalculator_data = BmiCalculator.objects.filter(user=request.user) 
    # return HttpResponse(serializers.serialize("json", bmicalculator_data), content_type='application/json')
    # handle for anonymous user
    if request.user.is_authenticated:
        bmicalculator_data = BmiCalculator.objects.filter(user=request.user) 
        return HttpResponse(serializers.serialize("json", bmicalculator_data), content_type='application/json')
    else:
        bmicalculator_data = BmiCalculator.objects.filter(user__isnull=True) 

        return HttpResponse(serializers.serialize("json", bmicalculator_data), content_type='application/json')


# @login_required(login_url='/login/')
def hapus_input(request, pk):
    if request.method == "DELETE":
        data = BmiCalculator.objects.get(pk=pk)
        data.delete()
        return JsonResponse({
            "pk" : data.pk,
            "fields" : {
                "weight" : data.weight,
                "height" : data.height,
                "bmi" : data.bmi,
                "date" : data.date,
                "status" : data.status,
            },
        },
        status=200
        )
        


# @login_required(login_url='/login/')
def add_calculate_ajax(request):
    if request.method == "POST":
        context = {}
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        bmi = float(weight) / ((float(height))/100 * (float(height))/100)
        user = request.user
        
        # handle for anonymous user
        if request.user.is_authenticated:
            data = BmiCalculator.objects.create(user=user, weight=weight, height=height, bmi=bmi, date=datetime.today())
            data.save()
            return JsonResponse({
                "pk" : data.pk,
                "fields" : {
                    "weight" : data.weight,
                    "height" : data.height,
                    "bmi" : data.bmi,
                    "date" : data.date,
                    "status" : data.status,
                },
            },
            status=200
            )
        else:
            data = BmiCalculator.objects.create(weight=weight, height=height, bmi=bmi, date=datetime.today())
            return JsonResponse({
            
                "pk" : 0,
                "fields" : {
                    "weight" : data.weight,
                    "height" : data.height,
                    "bmi" : data.bmi,
                    "date" : data.date,
                    "status" : data.status,
                },
            },
            status=200
            )




            
        




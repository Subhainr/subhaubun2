from django.shortcuts import render, redirect
from .models0 import TaskDb
from .forms0 import TaskForm

from .modelsML import TaskML
from .formsML import FormML

from django.contrib import messages
from django.http import HttpResponse
from . import prediction_file

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = TaskDb.objects.latest('id')
            messages.success(request, ('New item added..'))
            return render(request, 'result.html', {'all_items':all_items})
    else:
        all_items = TaskDb.objects.all()
        return render(request, 'index.html', {'all_items':all_items})

def ML_prediction(request):
    if request.method == 'POST':
        pclass = int(request.POST["pclass"])
        sex = int(request.POST["sex"])
        age = int(request.POST["age"])
        sibsp = int(request.POST["sibsp"])
        parch = int(request.POST["parch"])
        fare = float(request.POST["fare"])
        embarked = int(request.POST["embarked"])
        title = int(request.POST["title"])
        prediction = prediction_file.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
        form1 = FormML(request.POST or None )
        if form1.is_valid():
            form1.save()
            all_items1 = TaskML.objects.latest('id')
            messages.success(request, ('New item added..'))
            return render(request, 'ML_output.html', {'prediction':prediction,'all_items1':all_items1})
    else:
        all_items1 = TaskML.objects.all()
        return render(request, 'ML_prediction.html', {'all_items1':all_items1})

"""def output_prediction(request):
    pclass = int(request.GET["pclass"])
    sex = int(request.GET["sex"])
    age = int(request.GET["age"])
    sibsp = int(request.GET["sibsp"])
    parch = int(request.GET["parch"])
    fare = float(request.GET["fare"])
    embarked = int(request.GET["embarked"])
    title = int(request.GET["title"])
    prediction = prediction_file.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
    form2= FormML(request.GET or None)
    form2.save()
    all_items1 = TaskML.objects.latest('id')
    messages.success(request, ('New item added..'))
    return render(request, 'ML_output.html', {'prediction':prediction,'all_items1':all_items1})"""

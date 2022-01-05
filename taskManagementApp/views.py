from django.shortcuts import render, redirect
from . import prediction_file
from .modelsML import TaskML
from .formsML import FormML
from django.contrib import messages
from . import prediction_file
from django.conf import settings
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def camera(request):
    return render(request, 'camera.html')

def courses(request):
    return render(request, 'courses.html')

def elementary(request):
    return render(request, 'elementary.html')

def advanced(request):
    return render(request, 'advanced.html')

def rates(request):
    return render(request, 'rates.html')

def contact(request):
    return render(request, 'contact.html')


def result(request):
    First_name = request.GET['First_name']
    Second_name = request.GET['Second_name']
    email = request.GET['email']
    sw= request.GET['Reason']
    m = request.GET['TextBox']

    subject = 'Welcome to P.T. website'
    message = f'Hi, {First_name} {Second_name}, thank you for enquiring in our Private Tuition website. A notification has been sent to host successfully.\n{sw}\n{m}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, email_from]
    send_mail( subject, message, email_from, recipient_list )
    return render(request, 'result.html', {'First_name':First_name,'Second_name':Second_name,'email':email,'sw':sw,'m':m})

def ML_prediction(request):
    if request.method == 'POST':
        email = request.POST['email']
        Full_Name= request.POST['Full_Name']
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

            subject = 'Welcome to our Incredible world of Prediction'
            message = f'Hi, {Full_Name} congratulations for trying your prediction today. Why not, give more tries!\n{all_items1}\nResult: {prediction}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, email_from]
            send_mail( subject, message, email_from, recipient_list )

            return render(request, 'ML_output.html', {'prediction':prediction,'all_items1':all_items1})
    else:
        all_items1 = TaskML.objects.all()
        return render(request, 'ML_prediction.html', {'all_items1':all_items1})

#def ML_prediction(request):
        #return render(request, 'ML_prediction.html')

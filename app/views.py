from django.shortcuts import render

# Create your views here.
import json

file = open(r'D:\django\CAR\car.json','r')
json_data=file.read()
py_data=json.loads(json_data)

cars=py_data["cars"]
def home(request):
    context={
        'cars':cars
    }
    return render(request,'home.html',context )

def about(request,n):
    context={
        'cars':cars[n-1],   
    }
    return render(request,'about.html',context)


def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')
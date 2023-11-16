from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def indexPageView(request) :
    return render(request, 'homepages/index.html')

def aboutPageView(request) : 
    return render(request, 'homepages/about.html')

def empPageView(request) :
            data = Employee.objects.all()
        
            context = {
                "our_emps" : data
            }
            return render(request, 'homepages/displayEmps.html', context) 

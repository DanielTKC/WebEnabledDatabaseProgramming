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

def findEmpPageView(request) :
                return render(request, 'homepages/searchEmps.html')
            
def searchEmpPageView(request) :
                sFirst = request.GET['first_name']
                sLast = request.GET['last_name']
                data = Employee.objects.filter(emp_first=sFirst, emp_last=sLast)
            
                if data.count() == 0:
                    error_message = "Not Found"
                else:
                    error_message =""
                context = {
                        "our_emps" : data,
                        "message" : error_message
                    }
                return render(request, 'homepages/displayEmps.html', context)
                

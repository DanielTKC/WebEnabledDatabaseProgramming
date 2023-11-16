from django.shortcuts import render
from django.http import HttpResponse
from .models import State
from .models import Employee
from travelsites.models import Customer
from travelsites.models import Destination


# Create your views here.
def indexPageView(request):
    return render(request, "homepages/index.html")


def aboutPageView(request):
    return render(request, "homepages/about.html")


def empPageView(request):
    data = Employee.objects.all()

    context = {"our_emps": data}
    return render(request, "homepages/displayEmps.html", context)


def findEmpPageView(request):
    return render(request, "homepages/searchEmps.html")


def searchEmpPageView(request):
    sFirst = request.GET["first_name"]
    sLast = request.GET["last_name"]
    data = Employee.objects.filter(emp_first=sFirst, emp_last=sLast)

    if data.count() == 0:
        error_message = "Not Found"
    else:
        error_message = ""
    context = {"our_emps": data, "message": error_message}
    return render(request, "homepages/displayEmps.html", context)


def addEmpPageView(request):
    states = State.objects.all()
    context = {
        "states": states,
        "titles": [
            ("Ms.", "MISS"),
            ("Mr.", "MR."),
            ("Mrs.", "MRS."),
            ("Miss", "Miss"),
            ("Mx.", "MX."),
        ],
    }

    return render(request, "homepages/addEmps.html", context)


def storeEmpPageView(request):
    # Check to see if the form method is a get or post
    if request.method == "POST":
        # Create a new employee object from the model (like a new record)
        new_employee = Employee()

        # Store the data from the form to the new object's attributes (like columns)
        new_employee.emp_first = request.POST.get("emp_first")

        # You could have also used:
        # new_employee.emp_first = request.POST['emp_first']

        new_employee.emp_last = request.POST.get("emp_last")
        new_employee.emp_title = request.POST.get("emp_title")

        # Get all of the State objects (record or records) for the current employee state
        new_state = State.objects.get(state_abbrev=request.POST.get("emp_state"))

        # Create a new Contact Information object (record)
        new_contact = Contact_Information()

        # Store the data from the form to the contact phone attribute (column)
        new_contact.contact_phone = request.POST.get("contact_info")

        # Save the contact information record, which will generate the autoincremented id
        new_contact.save()

        # Store the newly created contact information id (object or record reference) to the employee record
        new_employee.contact_information = new_contact

        # Store the State reference found to the employee state
        new_employee.emp_state = new_state

        # Save the employee record
        new_employee.save()

    # Make a list of all of the employee records and store it to the variable
    data = Employee.objects.all()

    # Assign the list of employee records to the dictionary key "our_emps"
    context = {"our_emps": data}
    return render(request, "homepages/displayEmps.html", context)

def showCustomersPageView(request) :
    data = Customer.objects.all()

    context = {
        "cust" : data
    }
    return render(request, 'homepages/showCustomers.html', context)

def showSingleCustomerPageView(request, cust_id) :
    data = Customer.objects.get(id = cust_id)
    destinations = data.destinations.all()

    context = {
        "record" : data,
        "dest" : destinations
    }
    return render(request, 'homepages/editCustomer.html', context)

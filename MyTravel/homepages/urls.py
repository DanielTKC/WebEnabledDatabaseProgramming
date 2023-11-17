from django.urls import path 
from .views import indexPageView
from .views import aboutPageView
from .views import empPageView
from .views import searchEmpPageView
from .views import findEmpPageView
from .views import addEmpPageView
from .views import storeEmpPageView
from .views import showCustomersPageView
from .views import showSingleCustomerPageView
from .views import updateCustomersPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("emp/", empPageView, name="employee"),
    path("searchemp/", searchEmpPageView, name="searchemp"),
    path("findemp/", findEmpPageView, name="findemp"), 
    path("addemp/", addEmpPageView, name="addemp"),  
    path("storeemp/", storeEmpPageView, name="storeemp"),
    path("customers/" , showCustomersPageView, name="customers"),
    path("showCustomers/<int:cust_id>/" , showSingleCustomerPageView, name="showSingleCustomer"),
    path("updateCustomers/", updateCustomersPageView, name="updateCust"),
]


from django.urls import path 
from .views import indexPageView
from .views import aboutPageView
from .views import empPageView
from .views import searchEmpPageView
from .views import findEmpPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("emp/", empPageView, name="employee"),
    path("searchemp/", searchEmpPageView, name="searchemp"),
    path("findemp/", findEmpPageView, name="findemp"), 
]


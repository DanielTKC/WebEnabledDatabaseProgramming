from django.urls import path 
from .views import indexPageView
from .views import aboutPageView
from .views import empPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("emp/", empPageView, name="employee"),
]


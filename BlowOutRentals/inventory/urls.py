from django.urls import path
from .views import instrumentPageView

            
urlpatterns = [
                path("", instrumentPageView, name="inventory"),
                   
            ]  
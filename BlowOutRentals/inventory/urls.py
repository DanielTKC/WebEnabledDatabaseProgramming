from django.urls import path
from .views import instrumentPageView
from .views import trumpetPageView

            
urlpatterns = [
                path("", instrumentPageView, name="inventory"),
                path("<str:instrument_name>/<int:value>/", trumpetPageView, name="trumpet_detail"),
                
                   
            ]  
from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'travelpages/index.html')   

# Create your views here.
def aboutPageView(request, trip_name, trip_length) :
    context = {
        "trip_name" : trip_name,
        "trip_length" : trip_length + 2,
        "places_to_visit" : ["Arenal Volcano", "Manual Antonio National Park", "Monteverde Cloud Forest"]  
    }  

    return render(request, 'travelpages/about.html', context)
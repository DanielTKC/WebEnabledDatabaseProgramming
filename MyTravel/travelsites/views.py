from django.shortcuts import render
from django.shortcuts import HttpResponse

def showTripsPageView(request) :
    return render(request, 'travelsites/showTrips.html')

def showAfricaPageView(request) :
    context = {
        "area" : "Africa"
    }
    return render(request, 'travelsites/displayTrips.html', context)

def showAsiaPageView(request) :
    context = {
        "area" : "Asia"
    }
    return render(request, 'travelsites/displayTrips.html', context)

def showAustraliaPageView(request) :
    context = {
        "area" : "Australia"
    }
    return render(request, 'travelsites/displayTrips.html', context)

def showEuropePageView(request) :
    context = {
        "area" : "Europe"
    }
    return render(request, 'travelsites/displayTrips.html', context)

def showNorthAmericaPageView(request) :
    context = {
        "area" : "North America"
    }
    
    return render(request, 'travelsites/displayTrips.html', context)

def showSouthAmericaPageView(request) :
    context = {
        "area" : "South America"

    }
    
    return render(request, 'travelsites/displayTrips.html', context)
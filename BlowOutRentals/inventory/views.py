from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def instrumentPageView(request):
    return render(request, "inventory/instruments.html")

def trumpetPageView(request, instrument_name, value):
    # Pass the parameters to the template
    context = {
        'instrument_name': instrument_name,
        'value': value,
    }
    return render(request, "inventory/trumpet.html", context)
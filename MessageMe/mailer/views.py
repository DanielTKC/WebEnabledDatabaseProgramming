from django.shortcuts import HttpResponse

# Create your views here.
def indexPageView(request) :
    sOutput = '<html><head><title>Vandelay Industries</title></head><body><div class="container" style="text-align:center;"><div style="padding:60px; background:#1abc9c; color:white; font-size:30px;"><h1>Welcome to Vandelay Industries</h1><p>We Are The Number One Importer Exporter In All Of Kansas City!</p></div><div style="padding:50px;background-color:#90E2D2;"><h2>Make sure to check out our about section and contact us today!</h2></div></div></body></html>'
    return HttpResponse(sOutput)

def aboutPageView(request) :
    sOutput = '<html><head><title>Vandelay Industries</title></head><body><div class="container" style="text-align:center;"><div style="padding:60px; background:#1abc9c; color:white; font-size:30px;"><h1>Welcome to Vandelay Industries</h1><p>We Are The Number One Importer Exporter In All Of Kansas City!</p></div><div style="padding:50px;background-color:#90E2D2;"><h3 style="margin:16;">About Us</h3><p>What ever you need imported or exported our team is there</p><ul style="padding:0; list-style-type:none; "><li>New Items</li><li>Old Items</li><li>Religious Artifacts</li></ul><p>We simply do NOT care</p></div></div></body></html>'
    return HttpResponse(sOutput)

def contactPageView(request, first_name, last_name, email_address) :
        sOutput = f'<html><head><title>Vandelay Industries</title></head><body><div class="container" style="text-align:center;"><div style="padding:60px; background:#1abc9c; color:white; font-size:30px;"><h1>Welcome to Vandelay Industries</h1><p>We Are The Number One Importer Exporter In All Of Kansas City!</p></div><div style="padding:50px;background-color:#90E2D2;"><h2>{first_name} {last_name}, we will contact you at {email_address}</h2></div></div></body></html>'
        return HttpResponse(sOutput)
from django.shortcuts import render,redirect
import pywhatkit
import webbrowser as web
from urllib.parse import quote
from django.http import HttpResponse
import time

# Create your views here.


def home(request):
    return render (request,'base.html')

def data_submit(request):
        if request.method=="POST":
            cname=request.POST.get('cname')
            city=request.POST.get('city')
            mobile=request.POST.get('mobile')
            addr=request.POST.get('addr')
            detail=cname+" "+addr+" "+ city
            try:
                web.open(f"https://web.whatsapp.com/send?phone={mobile}&text={quote(detail)}",new=2)
                return redirect ("home")
            except:
                HttpResponse ("Not Able to Open")
        else:
            return HttpResponse("Something is Wrong")    
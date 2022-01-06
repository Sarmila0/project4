from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request,"myblog/home.html")

def contact(request):
    if request.method=="POST":
        name1=request.POST["myname"]
        email1=request.POST["myemail"]
        address1=request.POST["myaddress"]
        message1=request.POST["mymessage"]
        contactobject=Contact(name=name1, email=email1, address=address1, message8=message1)
        contactobject.save()
    return render(request,"myblog/contact.html")

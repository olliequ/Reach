from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "website/homepage.html")
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"] #get post data in the thing called 'username'
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("caught")
            return HttpResponseRedirect(reverse("website:homepage"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid." 
            })    
    
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("website:homepage"))    
    return render(request, "users/login.html")

def logout_view(request):
    logout(request) 
    return render(request, "website/landing.html", {
        "message": "You have been succesfully logged out."
    })

def error_404_view(request, exception):
    return render(request, 'website/404.html') 
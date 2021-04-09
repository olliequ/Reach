from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from .models import Flight, Airport, Passenger, User, Mood, Feeling, Meetings, Meals, Sleep
import datetime 


class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task") #widget=forms.TextInput(attrs={'class' : 'llabel'})

# Create your views here.
def index(request): #this index represents a view. When should we return this function/response? We do this in urls.py.
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("website:homepage"))

    return render(request, "website/landing.html") 

def homepage(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
            "message": "You have to log in to see this content!"
        })   
         
    return render(request, "website/homepage.html")

def user_login(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            print("we here.")
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("website:index")) #figure out what the URL for the index page in the website app is, and use that URL redirect to.
        else:
            return render(request, "website/login2.html", {
                "form": form
            })
    
    return render(request, "website/login2.html", {
        "form": NewTaskForm()
    })

def signup(request):
    if request.method == "POST":
        firstname = request.POST["firstname"] #get post data in the thing called 'username'
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        country = request.POST["country"]
        if (User.objects.filter(username=username).exists()):
            print("Sorry, username taken.")
            return render(request, "website/signup.html", {
                "message": "This username already exists!" 
            })
        
        user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
        user1 = authenticate(request, username=username, password=password)
        if user1 is not None:
            login(request, user1)
            return HttpResponseRedirect(reverse("website:homepage"))

        else:
            return render(request, "website/signup.html", {
                "message": "Something went wrong." 
            })

    if request.user.is_authenticated:
        return render(request, "website/homepage.html", {
            "message": "You're already logged in, there's no need to sign up. If you want to make a new account, please log out first."
        })     
    return render(request, "website/signup.html")

def meditate(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
            "message": "You have to log in to see this content!"
        })
    return render(request, "website/meditate.html")

def mood(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
            "message": "You have to log in to see this content!"
        })

    return render(request, "website/newmood.html")

def todaysmood(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
            "message": "You have to log in to see this content!"
        })

    return render(request, "website/todaysmood.html", {
        "moods": Mood.objects.filter(username=request.user.username).last() 
    })  

def moodlogs(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
            "message": "You have to log in to see this content!"
        })

    if  'submitbutton' in request.POST:
        xmood = request.POST["mood"]
        print(xmood)
        xsleep = request.POST["sleep"]
        print(xsleep)
        xmeals = request.POST["meals"]
        print(xmeals)
        xpeople = request.POST["people"]
        print(xpeople)
        description = request.POST["description"]
        print(f"you, in a {xmood} mood, slept for {xsleep}, ate {xmeals}, met {xpeople}, and wrote: {description}")
        foo_instance = Mood.objects.create(username=request.user.username, date=datetime.datetime.now(), mood=Feeling.objects.get(id=xmood), sleep=Sleep.objects.get(id=xsleep), meals=Meals.objects.get(id=xmeals), meetings=Meetings.objects.get(id=xpeople), diary=description)
        #user = request.user.id 
        #print(Mood.objects.filter(username=request.user.username).last().id)
        print(f"you, in a {mood} mood, wrote: {description}")
        return render(request, "website/moodlogs.html", {
            "message": Mood.objects.filter(username=request.user.username).last(),
            "moods": Mood.objects.filter(username=request.user.username),
            "user_id": request.user.id   
        })

    elif 'xbutton' in request.POST:
        value = request.POST["xbutton"]
        print(value)
        Mood.objects.filter(username=request.user.username, id=value).delete()
        return render(request, "website/moodlogs.html", {
            "message_two": Mood.objects.filter(username=request.user.username).last(),
            "moods": Mood.objects.filter(username=request.user.username),
            "user_id": request.user.id   
        })        

    return render(request, "website/moodlogs.html", {
        "moods": Mood.objects.filter(username=request.user.username),
        "user_id": request.user.id  
    }) 

def moodedit(request, user_id, mood_id):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
            "message": "You have to log in to see this content!"
        })

    entry = Mood.objects.filter(username=request.user.username).order_by('id')[mood_id]
    return render(request, "website/editentry.html", {
        "mood": entry 
    }) 

def resources(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
            "message": "You have to log in to see this content!"
        })
    return render(request, "website/resources.html")

def aboutus(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))    
    return render(request, "website/aboutus.html")

def error(request):
    return render(request, "website/404.html", {
        "flights": Flight.objects.all(),
        "passengers": Passenger.objects.all() 
    })  

def error_404_view(request, exception):
    return render(request, 'website/404.html')  
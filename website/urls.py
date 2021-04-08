# Each app has its own URLs.py (made myself) to control what URLs are available for each particular app. 

from django.urls import path

from . import views

app_name = "website"
urlpatterns = [                         # List of allowable URLs that can be accessed for this particular app.
    path("", views.index, name="index"), # Route/url, and what view (and function there) that should be rendered when said route/URL is visited.
    path("homepage", views.homepage, name="homepage"),                                    # Giving a 'name' to a particular url pattern (path) makes it easier to reference later.
    path("login", views.user_login, name="login"),
    path("signup", views.signup, name="signup"),
    path("meditate", views.meditate, name="meditate"),
    path("resources", views.resources, name="resources"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("error", views.error, name="error"),
    path("mood", views.mood, name="mood"),
    path("todaysmood", views.todaysmood, name="todaysmood"),
    path("moodlogs", views.moodlogs, name="moodlogs"),
    path("<int:user_id>/<int:mood_id>", views.moodedit, name="moodedit")  
]
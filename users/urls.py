from django.urls import path

from . import views

app_name = "users"
urlpatterns = [                         # List of allowable URLs that can be accessed for this particular app.
    path("", views.index, name="index"), # Route/url, and what view (and function there) that should be rendered when said route/URL is visited. 
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]
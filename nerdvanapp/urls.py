from django.urls import path
from nerdvanapp import views


urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('logged-user', views.UserView.as_view()),
    path('logount', views.LogoutView.as_view())
]

from django.urls import path
from nerdvanapp.views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logged-user', UserView.as_view()),
    path('logount', LogoutView.as_view())
]

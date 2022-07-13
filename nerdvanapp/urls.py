from django.urls import path
from nerdvanapp import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('validate-password', views.LoginView.as_view()),
    path('logged-user', views.UserView.as_view()),
    path('logount', views.LogoutView.as_view())
]

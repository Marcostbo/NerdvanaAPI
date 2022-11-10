from django.urls import path
from nerdvanapp import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Register routes
    path('register', views.RegisterView.as_view()),
    path('email-validate', views.SendEmailValidateCodeView.as_view()),
    path('email-validate/user', views.ValidateEmailView.as_view()),
    # Authentication routes
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    # User routes
    path('validate-password', views.LoginView.as_view()),
    path('logged-user', views.UserView.as_view()),
    path('logout', views.LogoutView.as_view()),
    # Game routes
    path('games', views.GameListView.as_view()),
    path('games/<int:pk>/', views.GameView.as_view()),
    # Recommender routes
    path('recommender', views.GameRecommenderView.as_view()),
    # Game Pricing routes
    path('gamepricing', views.GamePricingView.as_view())
]

from django.urls import path, include
from nerdvanapp import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# Register routes
router.register(r'register', views.RegisterViewSet, basename='register')
# Price Alert routes
router.register(r'price-alert', views.PriceAlertViewSet, basename='price-alert')

urlpatterns = [
    # Routers from viewset
    path('', include(router.urls)),
    path('email/generate-code', views.SendEmailValidateCodeView.as_view()),
    path('email/validate-user', views.ValidateEmailView.as_view()),
    # Password Recovery routes
    path('password-recovery/generate-code', views.SendEmailPasswordRecoveryView.as_view()),
    # Authentication routes
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    # User routes
    path('validate-password', views.LoginView.as_view()),
    path('logged-user', views.UserView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('user/change-password', views.ChangePasswordView.as_view()),
    # Game routes
    path('games', views.GamesViewSet.as_view({'get': 'list'})),
    path('games/<int:pk>/', views.GamesViewSet.as_view({'get': 'retrieve'})),
    # Recommender routes
    path('recommender', views.GameRecommenderView.as_view()),
    # Game Pricing routes
    path('gamepricing', views.GamePricingView.as_view()),
]

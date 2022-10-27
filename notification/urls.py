from notification import views
from django.urls import path


urlpatterns = [
    # Generate code routes
    path('generate-code/password-recovery', views.GenerateValidPasswordCodeView.as_view()),
    path('generate-code/validate-email', views.GenerateValidEmailCodeView.as_view()),
]

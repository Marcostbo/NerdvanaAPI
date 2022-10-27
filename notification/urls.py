from notification import views
from django.urls import path


urlpatterns = [
    # Generate code routes
    path('generate-code', views.GenerateValidCodeView.as_view()),
]

from django.urls import path
from django.contrib.auth.views import LoginView
from .views import HomeView

urlpatterns = [
    path('custom-login/', LoginView.as_view(template_name='login.html'), name='custom_login'),
    path('', HomeView.as_view(), name='home'),
]
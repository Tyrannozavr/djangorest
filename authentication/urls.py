from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework import routers

app_name = 'authentication'

# router = routers.SimpleRouter()
# router.register(r'register', RegistrationAPIView, basename='register')
# router.register(r'login', LoginAPIView, basename='login')

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

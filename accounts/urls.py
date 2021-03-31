from django.urls import path, include
from django.contrib.auth.views import LoginView
from accounts.views import LoginViewCustom


urlpatterns = [
    path('login/', LoginViewCustom.as_view(), name="ptlogin" )
]
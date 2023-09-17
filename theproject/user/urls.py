from django.urls import path
from user import views

urlpatterns = [
    path("register/", views.registrationView, name="register"),
    path("login-user/", views.loginUser, name="login-user"),
    path("logout/", views.loginUser, name="logoutUser"),
]
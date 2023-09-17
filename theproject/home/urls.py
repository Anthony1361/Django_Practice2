from django.urls import path
from home import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.aboutPage, name='about'),
    path('blog/', views.blogPage, name='blog'),
    path('contact/', views.contactPage, name='contact'),
]
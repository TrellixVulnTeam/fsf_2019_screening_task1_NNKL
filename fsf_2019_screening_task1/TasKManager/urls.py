from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'TasKManager'

urlpatterns = [path('', views.LoginPage, name="login"),
               path('signup/', views.signUpPage, name="signup"),
               path('welcome/', views.welcomePage, name="welcomepage"),
               # path('invitations/', include('invitations.urls', namespace='invitations')),
]

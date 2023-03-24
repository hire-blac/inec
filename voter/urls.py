from django.urls import path
from . import views

urlpatterns = [
    path('<code:code>', views.show, name='show_voter'),
    path('register', views.register, name='register'),
]
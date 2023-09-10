from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    ]

# https://127.0.0.1:8000
# https://127.0.0.1:8000/about

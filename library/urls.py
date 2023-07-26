from django.urls import path

from library import views

urlpatterns = [
    path('test/', views.inicio),
    path('nosotros/', views.nosotros),
]
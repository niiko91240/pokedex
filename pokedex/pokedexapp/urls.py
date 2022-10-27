from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.insert_api, name="api"),
    path('index/', views.liste, name="liste"),
]
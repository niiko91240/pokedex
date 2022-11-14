from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('api/', views.insert_api, name="api"),
    path('list/', views.list, name="list"),
    path('home/', views.home, name="home"),
    path('detail/<int:id>/', views.detail, name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
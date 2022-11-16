from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('api/', views.insert_api, name="api"),
    path('list/', views.list, name="list"),
    path('home/', views.home, name="home"),
    path('teams/', views.teams, name="teams"),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('addTeam/',views.addTeam, name='addTeam'),
    path('delTeam/',views.deleteTeam, name='delTeam')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
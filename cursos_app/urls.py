from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
    path('crear', views.crear),
    path('eliminar/<int:id>', views.eliminar)
    ]
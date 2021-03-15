from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
    path('crear', views.crear),
    path('eliminar/<int:id>', views.eliminar),
    path('eliminar/no_eliminar/<int:id>', views.no_eliminar),
    path('eliminar/si_eliminar/<int:id>', views.si_eliminar),
    path('comentarios/<int:id>', views.comentarios),
    path('comentarios/comentar/<int:id>', views.comentar),
    ]
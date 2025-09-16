from django.urls import path, include
from . import views
from rest_framework import routers
from .api_views import ReservaViewSet

router = routers.DefaultRouter()
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    # Vistas normales (HTML)
    path('', views.reservas_home, name='reservas_home'),
    path('nueva/', views.nueva_reserva, name='nueva_reserva'),
    path('editar/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),
    path('eliminar/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
    path('obtener-instructores/', views.obtener_instructores, name='obtener_instructores'),

    # API REST
    path('api/', include(router.urls)),
]


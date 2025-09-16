from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Reserva, Deporte, Instructor

class ReservaSerializer(serializers.ModelSerializer):
    # Para mostrar nombres en la respuesta
    deporte_nombre = serializers.StringRelatedField(source="deporte", read_only=True)
    instructor_nombre = serializers.StringRelatedField(source="instructor", read_only=True)
    estudiante_nombre = serializers.StringRelatedField(source="estudiante", read_only=True)

    # Para permitir enviar IDs al crear/editar
    deporte = serializers.PrimaryKeyRelatedField(queryset=Deporte.objects.all(), write_only=True)
    instructor = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all(), write_only=True)
    estudiante = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Reserva
        fields = [
            'id',
            'deporte', 'deporte_nombre',
            'instructor', 'instructor_nombre',
            'fecha', 'hora',
            'estudiante', 'estudiante_nombre',
        ]

        depth = 1  # muestra datos relacionados (ej. nombre del instructor)

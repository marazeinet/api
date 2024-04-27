from.models import Empleados
from rest_framework import serializers


class EmpleadosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('id', 'identificacion', 'nommbres',
                  'apellido', 'correo', 'salario_base', 'activo')
 #read_only_fieds = ('id', '')       
from dataclasses import field, fields
from rest_framework import serializers
from employee.models import Poste, Employe

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        field = '__all__'

class PosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = '__all__'
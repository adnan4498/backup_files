from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from test1.models import Student

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
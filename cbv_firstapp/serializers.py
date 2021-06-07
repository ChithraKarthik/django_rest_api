from rest_framework import serializers
from . models import StudentList,MarkList
class MarkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkList
        fields = '__all__'

class StudentListSerializer(serializers.ModelSerializer):
    marks = MarkListSerializer(read_only= True,many = True)
    class Meta:
        model = StudentList
        fields = "__all__"


from django.shortcuts import render
from . models import StudentList,MarkList
from . serializers import StudentListSerializer, MarkListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

class StudentListall(APIView):

    def get(self,request):
        student = StudentList.objects.all()
        serializer = StudentListSerializer(student, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarkListall(APIView):
    
    def get(self,request):
        studentmark = MarkList.objects.all()
        serializer = MarkListSerializer(studentmark, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MarkListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentListDetail(APIView):
    def get_object(self,pk):
        try:
           return StudentList.objects.get(pk=pk)
        except StudentList.DoesNotExist:
            raise Http404
    def get (self,request,pk):
        student = self.get_object(pk)
        serializer = StudentListSerializer(student)
        return Response(serializer.data)

    def put(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentListSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MarkListDetail(APIView):
    def get_object(self,pk):
        try:
            return  MarkList.objects.get(pk=pk)
        except MarkList.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        mark = self.get_object(pk)
        serializer = MarkListSerializer(mark)
        return Response (serializer.data)
    
    def put(self,request,pk):
        mark = self.get_object(pk)
        serializer = MarkListSerializer(mark)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        mark = self.get_object(pk)
        mark.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)




from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from core.serializers import StudentSerializer

#authentecting 
from rest_framework.permissions import IsAuthenticated

# from .serializers import StudentSerializer
from core.models import Student

class TestView(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get (self, request, *args, **kwargs):
        qs = Student.objects.all()
        Student1 = qs.first()
        serializer = StudentSerializer(Student1)
        return Response(serializer.data)
    
    
    def post (self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
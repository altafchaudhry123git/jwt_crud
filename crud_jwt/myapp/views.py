from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


# Create your views here.
class StudentApi(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self, request, id=None, format=None):
        if id is not None:
            data=Student.objects.get(id=id)
            serializer=StudentSerializer(data)
            return Response(serializer.data)
        data=Student.objects.all()
        serializer=StudentSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def put(self, request, id, format=None):
        record=Student.objects.get(id=id)
        serializer=StudentSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, id):
        record=Student.objects.get(id=id)
        record.delete()
        return Response('deleted')
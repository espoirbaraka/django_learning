from ast import Return
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from employee.models import *
from employee.serializers import *

# Create your views here.
@api_view(['GET'])
def posteList(request):
    poste = Poste.objects.all()
    poste_serializer = PosteSerializer(poste, many=True)
    return Response(poste_serializer.data)

@api_view(['POST'])
def posteCreate(request):
    poste_serializer = PosteSerializer(data=request.data)
    if poste_serializer.is_valid():
        poste_serializer.save()
        return Response(poste_serializer.data)
    return Response("Failed to save")

@api_view(['GET'])
def posteDetail(request, pk):
    poste = Poste.objects.get(posteId=pk)
    poste_serializer = PosteSerializer(poste, many=False)
    return Response(poste_serializer.data)
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from employee.models import *
from employee.serializers import *

# Create your views here.

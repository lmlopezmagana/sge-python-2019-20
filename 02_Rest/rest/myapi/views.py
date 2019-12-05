# from django.shortcuts import render
from astroid.scoped_nodes import objects
from rest_framework import viewsets

from .models import Hero
from .serializers import HeroSerializer

# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

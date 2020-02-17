from django.shortcuts import render

from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import PlanetSerializer
from .models import Planet


class PlanetView(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()
    permission_classes = (IsAuthenticated,)
    




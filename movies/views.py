from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie


# viewsets => auto CRUD
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

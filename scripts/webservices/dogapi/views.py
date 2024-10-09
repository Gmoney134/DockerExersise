from django.shortcuts import render
from rest_framework import generics
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer

class DogListCreateView(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class BreedListCreateView(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class BreedRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


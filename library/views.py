from django.shortcuts import render
from rest_framework import generics
from library.models import Book
from library.serializers import Bookserializer



class Booklist(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
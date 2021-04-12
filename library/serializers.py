from rest_framework import serializers
from library.models import Book


class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title', 'author', 'isbn', 'publisher',
                  #'image'
                   ]
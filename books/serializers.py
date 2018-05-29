from rest_framework import serializers

from .models import Category,Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Book
        fields = ('url','title','author','description','timestamp','category','owner')

class CategorySerialzer(serializers.HyperlinkedModelSerializer):
    #book = BookSerializer(read_only=True,many=True)
    class Meta:
        model = Category
        fields = ('url','pk','name','book')
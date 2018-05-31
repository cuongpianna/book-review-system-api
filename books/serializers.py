from rest_framework import serializers

from .models import Category,Book, Comment,Rate

class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.CharField(source='category.name')
    class Meta:
        model = Book
        fields = ('url','title','author','description','timestamp','category','owner')

class CategorySerialzer(serializers.HyperlinkedModelSerializer):
    #book = BookSerializer(read_only=True,many=True)
    class Meta:
        model = Category
        fields = ('url','pk','name','book')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.ReadOnlyField(source='book.title')
    owner = serializers.ReadOnlyField(source='owner.username')
    parrent = serializers.ReadOnlyField(source='parrent.pk')
    class Meta:
        model = Comment
        fields = ('url','book','owner','text','parrent')

class RateSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.ReadOnlyField(source='book.title')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Rate
        fields = ('url','book','owner','rate')
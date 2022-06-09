from rest_framework import serializers
from books import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):  
    category_name = serializers.ReadOnlyField(source='category.name')    
    class Meta:
        model = models.Books
        fields = '__all__'
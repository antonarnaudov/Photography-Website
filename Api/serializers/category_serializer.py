from rest_framework import serializers

from Photos.models.category_model import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

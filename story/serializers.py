from rest_framework import serializers
from models import Category, Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('Name', 'Description', 'Thumbnail')
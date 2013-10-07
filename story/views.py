from story.models import Category, Story
from django.views.generic.list import ListView
from django.shortcuts import render

class IndexView(ListView):
    template_name = 'story/index.html'
    def get_queryset(self): return Category.objects.all()

# serializer
from rest_framework import serializers

class StorySerializer(serializers.ModelSerializer):
    # custom field and serializer, u have to define method name like that get_xx 
    publishers = serializers.SerializerMethodField("get_publisher")
    def get_publisher(self, obj):   return "kim yong"
    
    class Meta:
        model = Story
        fields = ('name', 'publishers',) # we can customize like that.. 

class CategorySerializer(serializers.ModelSerializer):
    storys = StorySerializer()
    class Meta: model = Category
        
    def validate_name(self, attrs, source):
        posted_name = attrs.get(source, None)
        if posted_name and posted_name == "django":
            raise serializers.ValidationError("Not allowed category")
        
        return attrs

    
# add to rest code (MultipleObjectAPIView?)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

class CategoryListAPIView(ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    # filtering field by django-filter
    filter_fields = ('name', )

class CategorysRetrieveAPIView(RetrieveUpdateAPIView):
    model = Category
    serializer_class = CategorySerializer
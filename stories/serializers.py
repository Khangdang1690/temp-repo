from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
  model = Story
  fields = '__all__'
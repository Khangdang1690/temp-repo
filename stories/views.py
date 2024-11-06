from django.shortcuts import render
from rest_framework import viewsets
from .models import Story
from .serializers import StorySerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class StoryViewSet(viewsets.ModelViewSet):
  queryset = Story.objects.all() #This defines the data that the view will work with. Here, it retrieves all records from the Story model. When someone makes a request to this API, this queryset determines which stories are accessible.
  serializer_class = StorySerializer #This tells the viewset to use StorySerializer to handle data conversion. The serializer will convert Story instances into JSON format for API responses and handle incoming JSON data to create or update Story instances in the database.
  permission_classes = [AllowAny] #Allow any user to access the API

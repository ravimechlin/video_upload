from django.shortcuts import render,HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.viewsets import ModelViewSet
from . models import Video, CustomUser

from . serializer import VideoSerializer
from rest_framework.response import Response
from . mixins import *

# Create your views here.

class VideoViewset(BaseProjectViewset):


    queryset=Video.objects.all()
    serializer_class=VideoSerializer
    
    


    


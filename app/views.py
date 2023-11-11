from django.shortcuts import render,HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.viewsets import ModelViewSet
from . models import Video, CustomUser,TodoItem

from . serializer import VideoSerializer, TodoSerializer
from rest_framework.response import Response
from . mixins import *

from . tasks import *

# Create your views here.

class VideoViewset(BaseProjectViewset):


    queryset=Video.objects.all()
    serializer_class=VideoSerializer

class TodoItemViewset(BaseProjectViewset):
    queryset=TodoItem.objects.all()
    serializer_class=TodoSerializer





# def use_email(requst):
#     print("hello")
#     send_email_to_everyone.delay()
#     return HttpResponse("email is done")

    
    


    


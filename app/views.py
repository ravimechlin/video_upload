from django.shortcuts import render,HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.viewsets import ModelViewSet
from . models import Video, CustomUser

from . serializer import VideoSerializer
from rest_framework.response import Response
from . mixins import *

from . tasks import *
# Create your views here.

class VideoViewset(BaseProjectViewset):


    queryset=Video.objects.all()
    serializer_class=VideoSerializer


def use_email(requst):
    send_email_to_everyone.delay()
    return HttpResponse("email is done")

    
    


    


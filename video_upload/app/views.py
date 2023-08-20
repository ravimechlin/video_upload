from django.shortcuts import render,HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.viewsets import ModelViewSet
from . models import Video

from . serializer import VideoSerializer
from rest_framework.response import Response
# Create your views here.

class VideoViewset(ModelViewSet):

    queryset=Video.objects.all()
    serializer_class=VideoSerializer
    renderer_classes=[TemplateHTMLRenderer]

    template_name="index.html"
    def list(self, request, *args, **kwargs):
        videos = self.get_queryset()
        print(videos,"videos")
        
        return Response({'videos': videos})
    

    def create(self, request, *args, **kwargs):
        video_file = request.FILES.get('video_file')  
        if video_file:
            title = request.data.get('title') 
            video = Video.objects.create(title=title, video_file=video_file)
            serializer = self.serializer_class(video)
            return Response({'serializer': serializer})
        return super().create(request, *args, **kwargs)


    




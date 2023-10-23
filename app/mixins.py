from rest_framework import generics
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from  rest_framework.viewsets import ModelViewSet

class BaseProjectViewset(LoggingMixin,ModelViewSet):
    def get(self, request):
        return Response('with logging')
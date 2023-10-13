from rest_framework import serializers
from .models import Video,CustomUser




class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields="__all__"

class VideoSerializer(serializers.ModelSerializer):
    user_detail=CustomUserSerializer(source="user",read_only=True)

    class Meta:
        model=Video

        fields=[
            "title",
            "video_file",
            "user_detail",
            "created_at",
          
        ]
   
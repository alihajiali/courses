from elastic_transport import Serializer
from rest_framework import serializers
from .models import *

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ("name", "id")

class HashtagToPostSerializer(serializers.Serializer):
    hashtag_list = serializers.ListField()
    is_dupplicate = serializers.BooleanField()
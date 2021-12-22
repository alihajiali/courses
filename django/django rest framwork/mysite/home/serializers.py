from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    body = serializers.CharField()
    created = serializers.DateTimeField()


class StoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'title', 'body')
        extra_kwargs = {
            'title':{'help_text': 'this is title'}
        }

    # validate
    def validate_title(self, value):
        if value == 'testbook':
            raise serializers.ValidationError('title cant be testbook')
        return value
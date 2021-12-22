from rest_framework import serializers, viewsets
from .models import Story
from .serializers import StorySerializer, StoryModelSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


"""way1"""
# class StoryVieweset(viewsets.ModelViewSet):
#     queryset = Story.objects.all()
#     serializer_class = StorySerializer


"""way2"""
class StoryVieweset(viewsets.ViewSet):
    def list(self, request):                #localhost:8000/api/story   -> get
        queryset = Story.objects.all()
        serializers = StorySerializer(queryset, many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk):       #localhost:8000/api/story/(pk)  -> get
        queryset = get_object_or_404(Story, pk=pk)
        serializer = StorySerializer(queryset)
        return Response(serializer.data)

    def create(self, request):             #localhost:8000/api/story/   -> post
        serializer = StoryModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ok'})
        else :
            return Response()

    def update(self, request, pk):        #localhost:8000/api/story/(pk)/ -> put
        queryset = get_object_or_404(Story, pk=pk)
        serializer = StoryModelSerializer(data = request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            queryset.title=data['title']
            queryset.body=data['body']
            queryset.save()
            return Response({'message': 'ok'})
        else :
            return Response()

    def delete(self, request, pk):       #localhost:8000/api/story/3/  -> delete
        queryset = get_object_or_404(Story, pk=pk)
        queryset.delete()
        return Response({'message': 'ok'})
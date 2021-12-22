from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# simple get
@api_view(['GET'])
def test1(request):
    return Response({'name': 'Ali','family': 'HajiAli','age': 22,'city': 'Qom'}, status=status.HTTP_200_OK)


# get and post
@api_view(['GET', 'POST'])
def test2(request):
    if request.method == "POST":
        name = request.data['name']
        return Response({'name': f'my name is {name}'}, status=status.HTTP_201_CREATED)
    elif request.method == "GET":
        return Response({'name': 'my name is Ali'}, status=status.HTTP_200_OK)


# list get
from .models import Story
from .serializers import StorySerializer

@api_view()
def test3(request):
    story_data = Story.objects.all()
    ser_data = StorySerializer(story_data, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)


# single get
from django.shortcuts import get_object_or_404

@api_view()
def test4(request, id):
    story_data = get_object_or_404(Story, id = id)
    ser_data = StorySerializer(story_data)
    return Response(ser_data.data, status=status.HTTP_200_OK)


# create
from .serializers import StoryModelSerializer
from randomslugfield import RandomSlugField
from django.db import models

@api_view(["POST"])
def test5(request):
    info = StoryModelSerializer(data = request.data)
    if info.is_valid():
        '''way 1'''
        # data = info.validated_data
        # Story(title=data['title'], body=data['body']).save()
        '''way2'''
        info.save()
        return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)
    else :
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)


# update
@api_view(["POST"])
def test6(request, id):
    info = StoryModelSerializer(data = request.data)
    story = Story.objects.get(id=id)
    if info.is_valid():
        data = info.validated_data
        story.title=data['title']
        story.body=data['body']
        story.save()
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)
    else :
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)


# delete by permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

@api_view()
@permission_classes([IsAdminUser,])
def test7(request, id):
    story = Story.objects.get(id=id)
    story.delete()
    return Response({'message': 'ok'}, status=status.HTTP_200_OK)



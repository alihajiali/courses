from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from .documents import *
from .serializers import *
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

class PostViews(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        serdata = HashtagToPostSerializer(data = request.data)
        if serdata.is_valid():
            print("*"*80)
            s = PostDocument.search().filter("term", title='4')
            for hit in s:
                print("*"*80, hit.title)
            # hashtag_list = serdata.data["hashtag_list"]
            # post_list = []
            # for hashtag in hashtag_list:
            #     search_results = PostDocument.
            #     search().query("match", hashtag = hashtag)
            #     post_list.append(search_results)
            # print("*"*80, len(post_list))
            # print("*"*80, len(post_list))
        #     serializers = HashtagSerializer(data=search_results, many=True)
        #     for hit in serializers:
        #         print("*"*80, hit)
        #     if serializers.is_valid(raise_exception=True):
        #         return Response(serializers.data, status=status.HTTP_200_OK)
        # else:
        #     all_units = Hashtag.objects.all()
        #     serializers = HashtagSerializer(data=all_units)
        #     if serializers.is_valid():
        #         return Response(serializers.data, status=status.HTTP_200_OK)









        # s = HashtagDocument.search().filter("i" in "name")
  
        # for hit in s:
        #     print("*"*80, hit.name)
        #     return Response(hit.name)
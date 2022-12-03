from django.shortcuts import render

# Create your views here.
from exchange.models import Index
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
import math
from exchange.serializers import IndexSerializer


class IndexView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        scale = self.request.query_params.get("scale")
        now_timestamp = datetime.datetime.now()
        from_timestamp = now_timestamp - datetime.timedelta(days=7)
        indexes = Index.objects.filter(timestamp__gte=from_timestamp, timestamp__lte=now_timestamp)
        filtered_indexes = []
        for index in indexes:
            # todo do for all options
            # if index.timestamp.minute % 5 == 0:
            #     filtered_indexes.append(index)

            filtered_indexes.append(index)

        return Response(IndexSerializer(filtered_indexes, many=True).data)

    def post(self, request, format=None):
        serializer = IndexSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
from exchange.const import scales

class IndexView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        scale = scales.get(self.request.query_params.get("scale"), 60)
        to_timestamp = self.request.query_params.get("to")
        if not to_timestamp:
            to_timestamp = datetime.datetime.now()
        else:
            to_timestamp = datetime.datetime.fromtimestamp(to_timestamp)

        from_timestamp = self.request.query_params.get("from")
        if not from_timestamp:
            from_timestamp = to_timestamp - datetime.timedelta(days=7)
        else:
            from_timestamp = datetime.datetime.fromtimestamp(from_timestamp)

        indexes = Index.objects.filter(datetime__gte=from_timestamp, datetime__lte=to_timestamp)
        filtered_indexes = []
        for index in indexes:
            if index.datetime.timestamp() % scale == 0:
                filtered_indexes.append(index)

        return Response(IndexSerializer(filtered_indexes, many=True).data)

    def post(self, request, format=None):
        serializer = IndexSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

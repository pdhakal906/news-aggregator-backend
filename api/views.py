from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from itertools import zip_longest, chain
from .serializers import NewsSerializer
from .models import News


class ListNews(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        # Fetch all news from both sources
        setopati = News.objects.filter(source="setopati").order_by("-created_at")
        ekantipur = News.objects.filter(source="ekantipur").order_by("-created_at")

        # Combine the querysets maintaining the two-source structure
        combined_news = []

        # Use itertools to alternate between sources
        combined_news = list(chain.from_iterable(zip_longest(setopati, ekantipur)))

        # Remove any None values from the list
        combined_news = [item for item in combined_news if item is not None]

        return combined_news

    def list(self, request, *args, **kwargs):
        # Get the interleaved queryset
        queryset = self.get_queryset()

        # Use the pagination class from DRF
        page = self.paginate_queryset(queryset)

        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class TestView(APIView):
    def get(self, request, *args, **kwargs):

        return Response({"message": "Everything OK"}, status=status.HTTP_200_OK)

# from django.shortcuts import render
from hapi.music.models import Album
from rest_framework import viewsets
from hapi.music.serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Album.objects.all()     # .order_by('-date_joined')
    serializer_class = AlbumSerializer

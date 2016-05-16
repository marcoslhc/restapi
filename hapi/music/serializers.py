from models import Album
from rest_framework import serializers


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('artist', 'name', 'release_date', 'num_stars')

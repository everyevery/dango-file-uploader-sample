from rest_framework import serializers

from piklserver.uploader.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'created', 'file', 'name', 'description')
        read_only_fields = ('id', 'created', 'name')

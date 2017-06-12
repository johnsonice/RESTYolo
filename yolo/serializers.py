from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a a name field for testing our APIView."""
    name = serializers.CharField()

# class FileUploadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.FileUpload
#         fields = ('name','datafile')

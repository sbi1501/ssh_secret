from rest_framework import serializers


class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

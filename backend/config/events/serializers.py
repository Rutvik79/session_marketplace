from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'description',
            'creator',
            'created_at',
        )
        read_only_fields = ('creator', 'created_at')
from django.shortcuts import (render, get_object_or_404)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


from .models import Event
from .serializers import EventSerializer
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def event_list(request):
    # Public list
    if request.method == 'GET':
        events = Event.objects.all().order_by('-created_at')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    # creator-only create
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication required."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if request.user.role != "CREATOR":
            return Response(
                {"detail": "Only creators can create events."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    serializer = EventSerializer(event)
    return Response(serializer.data)


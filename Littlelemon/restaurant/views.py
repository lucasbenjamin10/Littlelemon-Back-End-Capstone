from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@permission_classes([IsAuthenticated])
class bookingview(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many= True)
        return Response(serializer.data) #Return JSON
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [IsAuthenticated]

class menuview(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = menuSerializer(items, many= True)
        return Response(serializer.data) #Return JSON
    
    def post(self, request):
        serializer = menuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data":serializer.data})
        
class menuitemsview(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class singlemenuitemsview(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

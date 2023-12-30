from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    queryset=Menu
    serializer_class=menuSerializer
    def get(self, request):
        items=self.queryset.objects.all()
        items=self.serializer_class(items, many=True)
        return Response(items.data, status=status.HTTP_200_OK)

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Menu
    serializer_class=menuSerializer
    def get(self, request, *args, **kwargs):
        pk=kwargs.get('pk')
        try:
            item=self.queryset.objects.get(pk=pk)
            item=self.serializer_class(item)
        except:
            return Response({'message':'DOES NOT EXIST'},status=status.HTTP_404_NOT_FOUND)
        return Response(item.data,status=status.HTTP_200_OK)
    

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes=[IsAuthenticated]
    def list(self, request, *args, **kwargs):
        try:
            items = self.queryset
            serializer = self.serializer_class(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'DOES NOT EXIST'}, status=status.HTTP_404_NOT_FOUND)

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})
from .models import MenuItem
from .serializers import MenuItemSerializer

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class MenuItemsView(APIView):
    def get(self,request):
        menu_items = MenuItem.objects.select_related('category').all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self,request):
        serializer = MenuItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SingleMenuItemView(APIView):
    def get(self,request,pk):
        menu_item = get_object_or_404(MenuItem,pk=pk)
        serializer = MenuItemSerializer(menu_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,pk):
        try:
            menu_item = MenuItem.objects.get(pk=pk)
            serializer = MenuItemSerializer(menu_item, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MenuItem.DoesNotExist:
            return Response({'error': 'true', 'message': 'Menu Item not found'}, status=status.HTTP_404_NOT_FOUND)
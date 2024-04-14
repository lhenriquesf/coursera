from .models import Book
from .serializers import BookSerializer

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

#@method_decorator(csrf_exempt,name='dispatch')
class BookView(APIView):
    def get(self,request):
        books = Book.objects.all().values()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class SingleBookView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book,pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'error': 'true', 'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
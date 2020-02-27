from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from . import models, serializers


# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class PostView(viewsets.ViewSet):
    serializer_class = serializers.PostSerializer

    def list(self, request):
        """HTTP GET /posts/"""
        queryset = models.Post.objects.all()
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            queryset,
            many=True,
            context=serializer_context
        )
        return Response(serializer.data)

    def create(self, request):
        """HTTP POST /posts/"""
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            data=request.data,
            context=serializer_context
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request):
        """HTTP GET /posts/<int:pk>"""
        pass

    def update(self, request):
        """HTTP PUT /posts/<int:pk>"""
        pass

    def destroy(self, request):
        """HTTP DELETE /posts/<int:pk>"""
        pass
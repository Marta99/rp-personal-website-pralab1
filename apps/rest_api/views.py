from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from . import models, serializers, permissions


# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class PostView(viewsets.ViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsReadOnlyOperation]       # for managing permissions

    def list(self, request):
        """ HTTP GET /posts/ """
        queryset = models.Post.objects.all()
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            queryset,
            many=True,
            context=serializer_context
        )
        return Response(serializer.data)

    def create(self, request):
        """ HTTP POST /posts/ """
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            data=request.data,
            context=serializer_context
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ HTTP GET /posts/<int:pk> """
        queryset = models.Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            post,
            context=serializer_context
        )
        return Response(serializer.data)

    def update(self, request, pk=None):
        """ HTTP PUT /posts/<int:pk> """
        queryset = models.Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            post,
            data=request.data,
            context=serializer_context
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, pk=None):
        """ HTTP DELETE /posts/<int:pk> """
        if models.Post.objects.filter(pk=pk).exists():
            post = models.Post.objects.get(pk=pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class CommentListView(APIView):
    serializer_class = serializers.CommentSerializer

    def get(self, request):
        """ HTTP GET /comments/ """
        queryset = models.Comment.objects.all()
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            queryset,
            many=True,
            context=serializer_context
        )
        return Response(serializer.data)


class CommentDetailView(APIView):
    serializer_class = serializers.CommentSerializer

    def get(self, request, pk=None):
        """ HTTP GET /comments/<int:pk>"""
        queryset = models.Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer_context = {'request': request}
        serializer = self.serializer_class(comment, context=serializer_context)
        return Response(serializer.data)

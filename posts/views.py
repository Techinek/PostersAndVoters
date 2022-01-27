from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, mixins, status, serializers
from rest_framework.response import Response

from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs.get('pk'))
        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):
        user = self.request.user
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        serializer.save(voter=user, post=post)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return serializers.ValidationError('You have no votes to delete')

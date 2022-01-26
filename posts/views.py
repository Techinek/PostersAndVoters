from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class VoteCreate(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        user = self.request.user
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        serializer.save(voter=user, post=post)

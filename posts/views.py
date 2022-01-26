from rest_framework import generics

from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class VoteList(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer



from django.urls import path

from .views import PostList, VoteList

urlpatterns = [
    path('posts/', PostList.as_view(), name='posts'),
    path('votes/', VoteList.as_view(), name='votes')
]

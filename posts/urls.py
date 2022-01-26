from django.urls import path

from .views import PostList, VoteCreate

urlpatterns = [
    path('posts/', PostList.as_view(), name='posts'),
    path('posts/<int:pk>/vote', VoteCreate.as_view(), name='votes')
]

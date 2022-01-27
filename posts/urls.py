from django.urls import path

from .views import PostDetail, PostList, VoteCreate

urlpatterns = [
    path('posts/', PostList.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='single_post'),
    path('posts/<int:pk>/vote', VoteCreate.as_view(), name='votes')
]

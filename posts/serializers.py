from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Post, Vote

USER = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')

    class Meta:
        model = Post
        fields = ('id', 'title', 'url', 'poster', 'poster_id', 'created')


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('id',)

    def validate(self, attrs):
        voter = get_object_or_404(USER, username=self.context['request'].user)
        post = get_object_or_404(
                Post,
                pk=self.context['request'].parser_context['kwargs'].get('pk'))
        if Vote.objects.filter(voter=voter, post=post).exists():
            raise serializers.ValidationError('Voter cannot vote twice')
        return attrs

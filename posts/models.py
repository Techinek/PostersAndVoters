from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

USER = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField()
    poster = models.ForeignKey(USER, on_delete=models.CASCADE,
                               related_name='posts')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='voted_posts')
    voter = models.ForeignKey(USER, on_delete=models.CASCADE,
                              related_name='voter_posts')

    class Meta:
        constraints = [
            UniqueConstraint(fields=['post', 'voter'], name='voter-posts')
        ]

    def __str__(self):
        return f"Voter: {self.voter.name} voted for {self.post}"

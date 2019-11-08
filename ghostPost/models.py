"""
Post Model:
    Boolean field whether Boast or Roast
    Charfield for post content
    integer field for up votes
    integer field or down votes
    datetimefield for submission time

"""

from django.db import models
from django.utils import timezone


class BoastnRoast(models.Model):
    boast = models.BooleanField(default=False)
    message = models.CharField(max_length=280)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    post_time = models.DateTimeField(default=timezone.now)
    total_votes = models.IntegerField(default=0)
    # @property
    # def total_votes(self):
    #     return self.upvote + self.downvote
    # vote_tally = total_votes

    def __str__(self):
        return f'{self.post_time},{self.message}'

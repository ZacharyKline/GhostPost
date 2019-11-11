"""
Post Model:
    Boolean field whether Boast or Roast
    Charfield for post content
    integer field for up votes
    integer field or down votes
    datetimefield for submission time

"""
import random
from django.db import models
from django.utils import timezone


def random_string():
    return str(random.randint(100000, 999999))


class BoastnRoast(models.Model):
    boast = models.BooleanField(default=False)
    message = models.CharField(max_length=280)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    post_time = models.DateTimeField(default=timezone.now)
    total_votes = models.IntegerField(default=0)
    secret_code = models.CharField(default=random_string, max_length=6)

    def __str__(self):
        return f'{self.post_time},{self.message}'

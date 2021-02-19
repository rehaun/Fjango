from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.CharField(max_length=10)
    name = models.CharField(max_length=15)
    email = models.EmailField()


class Tweet(models.Model):

    tweet_text = models.CharField(max_length=300).primary_key
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.tweet_text


class FollowingHearts(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    following_id = models.CharField(max_length=10)
    hearts = models.IntegerField()
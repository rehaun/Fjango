from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.CharField(max_length=10)
    name = models.CharField(max_length=15)
    email = models.EmailField()


class FollowingHearts(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    following_id = models.CharField(max_length=10)
    hearts = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(3), MinValueValidator(1)])


class Tweet(models.Model):
    tweet_id = models.CharField
    tweet_text = models.CharField(max_length=300).primary_key
    pub_date = models.DateTimeField('date published')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_cm = models.BooleanField
    parent_id = models.ForeignKey(tweet_id, on_delete= models.CASCADE)
    


    def __str__(self):
        return self.tweet_text


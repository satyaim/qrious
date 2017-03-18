from django.db import models
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User


class Player(models.Model):
    name = models.OneToOneField(User, null=True)
    score = models.IntegerField(default=0)
    question_no = models.IntegerField(default=1, blank=True)
    answers_given = models.CharField(max_length=100, default="000000")

    def __str__(self):
        return str(self.name)


class Questions(models.Model):
    question_no = models.IntegerField(blank=True, default=0)
    question = models.CharField(max_length=10000)
    solution = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.question_no)

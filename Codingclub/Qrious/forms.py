from django.contrib.auth.models import User
from django import forms
from .models import Questions


class AnswerForm(forms.Form):
    answerof = forms.CharField(max_length=10000)


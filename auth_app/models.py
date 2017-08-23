from django.forms import ModelForm
from django.db import models

class User(ModelForm):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    posts = []
    drafts = []
    likes = []

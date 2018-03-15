from django.contrib.auth.models import User as AuthUser
from django.db import models


class User(AuthUser):
    blog_name = models.CharField(max_length=100)

import datetime

from django import forms
from django.db import models
from django.utils import timezone


class NewPostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=300)
    image = forms.FileField(allow_empty_file=True, required=False)
    content = forms.CharField(widget=forms.Textarea)


class Post(models.Model):
    title = models.CharField(max_length=70)
    pub_date = models.DateField('date published')
    content = models.CharField(max_length=1500, default='')
    image = models.ImageField(blank=True)
    reblogs = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    source = 'TODO'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return 'Title: {0}, date: {1}'.format(self.title, self.pub_date)


class Note(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, default='')
    note_date = models.DateTimeField(
        'note\'s date', default=datetime.date(1995, 11, 17)
    )

    def __str__(self):
        pass


class Reblog(Note):
    def __str__(self):
        return 'reblog', self.post, self.username


class Like(Note):
    def __str__(self):
        return 'like', self.post, self.username

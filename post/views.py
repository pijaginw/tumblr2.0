import datetime

from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post, NewPostForm


def add_post(request):
    if request.method == 'GET':
        return render(request, 'post/form.html')

    elif request.method == 'POST':
        try:
            form = NewPostForm(request.POST, request.FILES)
            if form.is_valid():
                new_post = Post(
                    title=request.POST.get('title'),
                    image=request.FILES.get('image'),
                    content=request.POST.get('content'),
                    pub_date=datetime.datetime.today()
                )
                new_post.save()
                return render(None, 'dashboard/index.html', {'posts': Post.objects.all().order_by('-pub_date')})
            return render(request, 'post/form.html', {'error_msg': 'Something went wrong.'})
        except:
            raise forms.ValidationError("Something went wrong with adding new post!")


def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        return render(request, 'post/detail.html', {'post': post})
    except Post.DoesNotExist:
        raise get_object_or_404('There is nothing here')


def notes(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/notes.html', {'post': post})


def reblog(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        selected_post = post
    except(KeyError, Post.DoesNotExist):
        return render(request, 'post/detail.html', {
            'post': post,
            'error_message': 'You didn\'t select a post.',
        })
    else:
        selected_post.reblogs += 1
        selected_post.save()
        return HttpResponseRedirect(
            reverse('post:notes', args=(post.id,)))


def like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        selected_post = post
    except(KeyError, Post.DoesNotExist):
        return render(request, 'post/detail.html', {
            'post': post,
            'error_message': 'You didn\'t select a post.',
        })
    else:
        selected_post.likes += 1
        selected_post.save()
        return HttpResponseRedirect(
            reverse('post:notes', args=(post.id,)))

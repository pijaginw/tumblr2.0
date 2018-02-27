from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post


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

from django.shortcuts import render

from post.models import Post


def index(request):
    context = {'posts': Post.objects.all().order_by('-pub_date')}
    return render(request, 'dashboard/index.html', context)

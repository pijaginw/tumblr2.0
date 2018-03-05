from django.shortcuts import render

from post.models import Post


def index(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')
    context = {'latest_post_list': latest_post_list}
    return render(request, 'dashboard/index.html', context)

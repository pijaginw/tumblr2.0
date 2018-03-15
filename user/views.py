from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render

from post.models import Post


def login(request):
    if request.method == 'GET':
        return render(request, 'login_form.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'dashboard/index.html', {'posts': Post.objects.all().order_by('-pub_date')})
        else:
            return HttpResponse('<p>Oops! An error occured :-(</p>')


def logout(request):
    auth.logout(request)

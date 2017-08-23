# -*- coding=utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView

from .forms import LoginForm

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        # TODO: rozpoczęcie sesji
        print(form.cleaned_data['username'])
        print('>>>>>>>\n\n')
        return super(LoginView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        return render(request, 'auth_app/login.html')

    # def post(self, request, *args, **kwargs):
    #     try:
    #         print('\nw POSSSST\n')
    #         print(request)
    #     except Exception as e:
    #         raise
    #     else:
    #         return HttpResponseRedirect(
    #             reverse('dashboard:index', args=None))

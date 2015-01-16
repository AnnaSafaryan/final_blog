from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Post
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class Posts(View):
    def get(self, request):
        posts = Post.objects.filter(publish=True).order_by('-when')
        return HttpResponse(render(request, 'posts.html', {'posts': posts}))


class Login(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('No such login/password')


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponse('You succesfully logged out')
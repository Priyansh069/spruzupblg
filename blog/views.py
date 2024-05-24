from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # load all post from db(10)
    posts = Post.objects.all()[:11]
    slide = Post.objects.all()[:3]

    print(posts)
    print(slide)


    return render(request, 'home.html', {'posts': posts,'slides':slide})


def post(request, url):
    post = Post.objects.get(url=url)
    posts = Post.objects.all()[:3]
    # print(post)
    return render(request,'Post.html',{'post':post,'posts':posts})



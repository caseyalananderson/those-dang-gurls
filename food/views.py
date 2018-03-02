from django.shortcuts import render

from .models import BlogPost


# Create your views here.
def index(request):
    """
    Main index that displays blog post
    :param request:
    :return:
    """

    blog_posts = BlogPost.objects.all()

    context = {
        'blog_posts': blog_posts,
    }

    return render(request, 'blog/blog_list.html', context)


# Create your views here.
def blog_post(request, pk):
    """
    Main index that displays blog post
    :param request:
    :param pk
    :return:
    """

    post = BlogPost.objects.filter(pk=pk)[0]

    context = {
        'post': post,
    }

    return render(request, 'blog/blog_post.html', context)

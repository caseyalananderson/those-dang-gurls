from django.shortcuts import render

from .models import FoodEntry
from django.http import HttpResponse

# Create your views here.
def food_list(request):
    """
    Main index that displays blog post
    :param request:
    :return:
    """

    filter = request.GET.get('filter')

    if filter:
        food_posts = FoodEntry.objects.filter(filter)
    else:
        food_posts = FoodEntry.objects.all()

    print(food_posts)

    context = {
        'food_posts': food_posts,
    }

    return render(request, 'food/food_list.html', context)


# Create your views here.
def food_post(request, pk):
    """
    Main index that displays blog post
    :param request:
    :param pk
    :return:
    """

    post = FoodEntry.objects.filter(pk=pk)[0]

    context = {
        'post': post,
    }

    return render(request, 'food/food_post.html', context)

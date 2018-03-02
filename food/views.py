from django.shortcuts import render

from .models import FoodEntry


# Create your views here.
def food_list(request):
    """
    Main index that displays blog post
    :param request:
    :return:
    """

    filter_val = str(request.GET.get('filter'))
    print(filter_val)

    if filter_val == 'breakfast':
        food_posts = FoodEntry.objects.filter(breakfast=True)
    elif filter_val == 'vegan':
        food_posts = FoodEntry.objects.filter(vegan=True)
    elif filter_val == 'entree':
        food_posts = FoodEntry.objects.filter(entree=True)
    elif filter_val == 'snack':
        food_posts = FoodEntry.objects.filter(snack=True)
    else:
        food_posts = FoodEntry.objects.filter()

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

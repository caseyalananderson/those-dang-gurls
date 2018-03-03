from django.shortcuts import render

from .models import FoodEntry


# Create your views here.
def food_list(request):
    """
    Main index that displays blog post.
    Grabs "filter" from cookies in order to filter the query of the database
    :param request:
    :return:
    """

    # get the name of the string called "filter"
    food_filter = str(request.GET.get('filter'))

    # Select only the objects in the database that match the filter
    if food_filter:
        if food_filter == 'breakfast':
            food_posts = FoodEntry.objects.filter(breakfast=True).filter(published=True)
        elif food_filter == 'entree':
            food_posts = FoodEntry.objects.filter(entree=True).filter(published=True)
        elif food_filter == 'snack':
            food_posts = FoodEntry.objects.filter(snack=True).filter(published=True)
        elif food_filter == 'foodprep':
            food_posts = FoodEntry.objects.filter(foodprep=True).filter(published=True)
        elif food_filter == 'beverage':
            food_posts = FoodEntry.objects.filter(snack=True).filter(published=True)

        elif food_filter == 'vegan':
            food_posts = FoodEntry.objects.filter(vegan=True).filter(published=True)
        elif food_filter == 'vegetarian':
            food_posts = FoodEntry.objects.filter(vegan=True).filter(published=True)
        elif food_filter == 'glutenfree':
            food_posts = FoodEntry.objects.filter(vegan=True).filter(published=True)
        else:
            food_posts = FoodEntry.objects.filter().filter(published=True)
    else:
        food_posts = FoodEntry.objects.filter().filter(published=True)

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

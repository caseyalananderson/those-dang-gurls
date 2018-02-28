from django.shortcuts import render


# Stuff to search
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView
from recipes.models import Recipe


# Create your views here.
def index(request):
    """
    Main index that displays blog post
    :param request:
    :return:
    """

    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'recipes/recipe_list.html', context)


# Create your views here.
def recipe_detail(request, pk):
    """
    Main index that displays blog post
    :param request:
    :param pk
    :return:
    """

    recipe = Recipe.objects.filter(pk=pk)[0]

    context = {
        'recipe': recipe,
    }

    return render(request, 'recipes/recipe_detail.html', context)


from django.shortcuts import render

from .models import Recipe


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

    return render(request, 'recipes/recipes.html', context)

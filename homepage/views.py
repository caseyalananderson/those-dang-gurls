from django.shortcuts import render
from food.models import FoodPost
from fitness.models import FitnessPost
from travel.models import TravelPost
from beauty.models import BeautyPost
from itertools import chain
from operator import attrgetter


# Create your views here.
def homepage(request):

    last_post, recent_posts = get_recent_posts()

    context = {
        'last_post': last_post,
        'recent_posts': recent_posts,
    }

    return render(request, 'homepage.html', context)


# def order_by_post_date

def get_recent_posts():
    """
    Gets the recent posts
    :param request:
    :return:
    """
    food_posts = FoodPost.objects.published().order_by('-timestamp')
    fitness_posts = FitnessPost.objects.published().order_by('-timestamp')
    travel_posts = TravelPost.objects.published().order_by('-timestamp')
    beauty_posts = BeautyPost.objects.published().order_by('-timestamp')

    sorted_posts = sorted((chain(food_posts, fitness_posts, travel_posts, beauty_posts)),
                          key=attrgetter('timestamp'), reverse=True)

    return sorted_posts[0], sorted_posts[1:5]




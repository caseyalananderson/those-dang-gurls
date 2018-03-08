from django.shortcuts import render
from food.models import FoodPost
from fitness.models import FitnessPost
from travel.models import TravelPost
from beauty.models import BeautyPost


# Create your views here.
def homepage(request):
    """
    :param request:
    :return:
    """
    food_list = FoodPost.objects.published().order_by('-timestamp')[0:4]
    for f in food_list:
        print(f)

    return render(request, 'homepage.html')


# def order_by_post_date


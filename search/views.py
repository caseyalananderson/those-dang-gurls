# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from food.models import FoodPost
from beauty.models import BeautyPost
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core.paginator import Paginator
from itertools import chain


def search(request):
    """
    Searches
    :param request:
    :return:
    """

    food_qs = FoodPost.objects.published()

    keywords = request.GET.get('search_box')
    if keywords:
        query = SearchQuery(keywords)
        title_vector = SearchVector('title', weight='A')
        content_vector = SearchVector('content', weight='B')
        vectors = title_vector + content_vector
        food_qs = food_qs.annotate(search=vectors).filter(search=query)
        food_qs = food_qs.annotate(rank=SearchRank(vectors, query)).order_by('-rank')

    paginator = Paginator(food_qs, 6)  # Show 3 contacts per page

    page_number = request.GET.get('page')
    if page_number is not None:
        pagnated_search_qs = paginator.page(page_number)
    else:
        pagnated_search_qs = paginator.page(1)

    context = {
        'search_qs': pagnated_search_qs,
    }

    print(context)

    return render(request, 'search/search_list.html', context)

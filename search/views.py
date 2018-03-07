# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from food.models import FoodPost, Recipe
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core.paginator import Paginator


def search(request):
    """
    Searches
    :param request:
    :return:
    """

    qs = FoodPost.objects.all()

    keywords = request.GET.get('search_box')
    if keywords:
        query = SearchQuery(keywords)
        title_vector = SearchVector('title', weight='A')
        content_vector = SearchVector('content', weight='B')
        vectors = title_vector + content_vector
        qs = qs.annotate(search=vectors).filter(search=query)
        qs = qs.annotate(rank=SearchRank(vectors, query)).order_by('-rank')

    paginator = Paginator(qs, 6)  # Show 3 contacts per page

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

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from recipes.models import Recipe
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView
from django.http import HttpResponse

# Create your views here.


def search(request):
    """
    Searches
    :param request:
    :return:
    """

    qs = Recipe.objects.all()

    keywords = request.GET.get('search_box')
    this_str = "<p> %s </p>" % keywords
    if keywords:
        query = SearchQuery(keywords)
        title_vector = SearchVector('title', weight='A')
        content_vector = SearchVector('content', weight='B')
        vectors = title_vector + content_vector
        qs = qs.annotate(search=vectors).filter(search=query)
        qs = qs.annotate(rank=SearchRank(vectors, query)).order_by('-rank')

    #CAA TODO: SWTICH TO POSTGRES, NOT SQLLITE!!!

    context = {
        'qs': qs,
    }

    print(context)

    # return HttpResponse(this_str)
    return render(request, 'search/search_list.html', context)
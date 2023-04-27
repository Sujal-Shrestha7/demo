from django.db.models import Q
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search_experts(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    skill = Skills.objects.filter(title__icontains=search_query)
    experts = Experts.objects.distinct().filter(Q(full_name__icontains=search_query) |
                                                Q(short_intro__icontains=search_query) |
                                                Q(skills__in=skill) |
                                                Q(position__icontains=search_query))

    return experts, search_query


def pagination_experts(request, experts, results):
    page = request.GET.get('page')
    experts = experts
    pagination = Paginator(experts, results)
    try:
        experts = pagination.page(page)
    except PageNotAnInteger:
        page = 1
        projects = pagination.page(page)
    except EmptyPage:
        page = pagination.num_pages
        projects = pagination.page(page)

    left_index = (int(page)-4)
    if left_index < 1:
        left_index = 1

    right_index = (int(page)+4)
    if right_index > pagination.num_pages:
        right_index = pagination.num_pages+1

    custom_range = range(left_index, right_index)
    return experts, custom_range

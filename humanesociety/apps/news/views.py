from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from .models import Entry

def entry_detail(request, year, month, day, slug):
    states = [0, 1] if request.user.is_staff else [1]
    entry = get_object_or_404(Entry,
        status__in=states, 
        date_created__year=year,
        date_created__month=month,
        date_created__day=day,
        slug=slug)

    return render(request, 'news/entry_detail.html', {
        'entry': entry
    })

def entry_list(request, template_name='news/entry_list.html', get_context=dict):
    states = [0, 1] if request.user.is_staff else [1]
    entry_list = Entry.objects.filter(
        status__in=states)

    paginator = Paginator(entry_list, 10)

    try:
        current_page = request.GET.get('page') or 1
        page = paginator.page(current_page)
    except InvalidPage:
        raise Http404()

    context = get_context()
    context.update({
        'paginator': paginator,
        'current_page': current_page,
        'page': paginator.page(current_page),
    })

    return render(request, template_name, context)

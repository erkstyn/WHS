from django.shortcuts import render

from apps.news.models import Entry

def homepage(request):
    return render(request, 'homepage.html', {
        'posts': Entry.objects.all()
        if request.user.is_staff else
        Entry.objects.filter(status=Entry.PUBLISHED)
    })

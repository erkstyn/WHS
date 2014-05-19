from django.shortcuts import render
from .models import BoardMember

def board_list(request):
    return render(request, 'board_members/list.html', {
        'staff': BoardMember.objects.all()
    })

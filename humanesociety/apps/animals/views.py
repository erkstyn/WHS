from .models import AdoptionCandidate, Species, Breed
from django.shortcuts import render, get_object_or_404
from django.core.pagination import Paginator

def adoption_detail(request, slug):
    adoption_states = range(0, 3 if request.user.is_staff else 2)
    candidate = get_object_or_404(AdoptionCandidate, 
        status__in=adoption_states,
        slug=slug
    )

    return render(request, 'animals/adoption_detail.html', {
        'candidate': candidate    
    })


def adoption_list(request, species=None, breed=None):
    adoption_states = range(0, 3 if request.user.is_staff else 2)
    candidate_list = AdoptionCandidate.objects.filter(
        status__in=adoption_states)

    if breed is not None:
        candidate_list = candidate_list.filter(
            breed__slug=breed)

    if species is not None:
        candidate_list = candidate_list.filter(
            breed__species__slug=species)

    paginatior = Paginator(candidate_list, 10)
    current_page = int(request.GET.get('page') or 1)
   
    all_breeds = Breed.objects.filter(
        adoptioncandidate__status__in=adoption_states
    )

    all_species = Species.objects.filter(
        breed__adoptioncandidate__status__in=adoption_states
    )

    AdoptionCandidate.objects.all()

    return render(request, 'animals/adoption_detail.html', {
        'paginatior': paginator,
        'current_page': current_page,
        'page': paginator.page(current_page),
        'current_breed': breed,
        'current_species': species,
        'all_breeds': breeds,
        'all_species': species,
    })

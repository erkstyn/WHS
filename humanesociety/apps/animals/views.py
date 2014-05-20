from .models import AdoptionCandidate, Species, Breed
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404

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
    adoption_states = [0, 2] if request.user.is_staff else [0]
    candidate_list = AdoptionCandidate.objects.filter(
        status__in=adoption_states)

    if breed is not None:
        candidate_list = candidate_list.filter(
            breed__slug=breed)
        breed = get_object_or_404(Breed, slug=breed)

    if species is not None:
        candidate_list = candidate_list.filter(
            breed__species__slug=species)
        species = get_object_or_404(Species, slug=species)

    paginator = Paginator(candidate_list, 10)

    try:
        current_page = request.GET.get('page') or 1
        page = paginator.page(current_page)
    except InvalidPage:
        raise Http404()

    all_breeds = Breed.objects.filter(
        adoptioncandidate__breed__species=species,
    ).distinct() if species is not None else []

    all_species = Species.objects.filter(
        breed__adoptioncandidate__status__in=adoption_states
    ).distinct()

    return render(request, 'animals/adoption_list.html', {
        'paginator': paginator,
        'current_page': current_page,
        'page': paginator.page(current_page),
        'current_breed': breed,
        'current_species': species,
        'all_breeds': all_breeds,
        'all_species': all_species,
    })

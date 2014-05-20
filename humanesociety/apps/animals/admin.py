from django.contrib import admin
from .models import (
    Species,
    Breed,
    AdoptionCandidate,
)


class AdoptionCandidateAdmin(admin.ModelAdmin):
    radio_fields = {
        'status': admin.HORIZONTAL,
    }

    def species(self, model_instance):
        return model_instance.breed.species

    radio_fields = {
        'sex': admin.VERTICAL,
        'status': admin.VERTICAL,
    }

    prepopulated_fields = {
        'slug': ('name', ),
    }

    search_fields = (
        'name',
        'breed__name',
        'breed__species__name',
    )

    list_display = (
        'name',
        'breed',
        'species',
        'good_with_pets',
        'good_with_kids',
        'status',
    )

    list_filter = (
        'status',
        'breed__species',
        'good_with_pets',
        'good_with_kids',
    )


class BreedAdmin(admin.ModelAdmin):
    pass


class SpeciesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Species, SpeciesAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(AdoptionCandidate, AdoptionCandidateAdmin)

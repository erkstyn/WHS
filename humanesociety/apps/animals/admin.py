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

    list_display = (
        'breed',
        'species',
        'good_with_pets',
        'good_with_kids',
        'status',
    )

    list_filter = (
        'good_with_pets',
        'good_with_kids',
        'status',
    )


class BreedAdmin(admin.ModelAdmin):
    pass


class SpeciesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Species, SpeciesAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(AdoptionCandidate, AdoptionCandidateAdmin)

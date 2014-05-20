from django.db import models
from apps.animals.managers import AdoptionCandidateManager


class Species(models.Model):
    """This model catalogues the available
    species the Humane Society has to deal with.
    For example, "Foxes", "Dogs", "Cats",
    "Marmots", etc.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'species'


class Breed(models.Model):
    """Breeds are a specialization of Species --
    "poodles", "norwegian forest cats", etc -- that
    imply a given **Species**.
    """
    species = models.ForeignKey(Species)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return '%s | %s' % (self.species.name, self.name)

    class Meta:
        ordering = ['-species__name', 'name']


class Animal(models.Model):
    SEXES = (
        (0, 'Female'),
        (1, 'Male'),
    )
    name = models.CharField(max_length=255)
    breed = models.ForeignKey(Breed)
    sex = models.IntegerField(choices=SEXES)
    age = models.IntegerField()
    neutered = models.NullBooleanField()
    has_shots = models.NullBooleanField()
    weight = models.FloatField(help_text="""
        Weight of the animal, in pounds.
    """, null=True, blank=True)

    bio = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class AdoptionCandidate(Animal):
    ADOPTION_STATES = (
        (0, 'Available'),
        (1, 'Adopted'),
        (2, 'Unpublished'),
    )

    photo = models.ImageField(upload_to='animals', null=True, blank=True)
    self_introduction = models.TextField(help_text="""
        A self-introduction paragraph. 40 words will be displayed on the list page, the rest will be displayed on the detail.
    """)
    slug = models.SlugField(unique=True, help_text="""
        The URL that this animal will be viewable at. No spaces. Ex.: rex_the_dog
    """.strip())
    available_on = models.DateTimeField()
    published = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=ADOPTION_STATES)
    good_with_pets = models.NullBooleanField()
    good_with_kids = models.NullBooleanField()

    objects = AdoptionCandidateManager()

    @models.permalink
    def get_absolute_url(self):
        return ('adoption_detail', [self.slug]) 

    def is_available(self):
        return self.status == 0

    class Meta:
        ordering = ['-published', ]

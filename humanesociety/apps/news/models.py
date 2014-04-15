from django.db import models


class Entry(models.Model):
    PUBLISHED = 1
    DRAFT = 0

    choices = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.URLField(null=True, blank=True)
    status = models.IntegerField(choices=choices)

    date_created = models.DateTimeField(auto_now_add=True)
    tease = models.TextField(null=True, blank=True)
    body = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'
        ordering = ['-date_created', ]

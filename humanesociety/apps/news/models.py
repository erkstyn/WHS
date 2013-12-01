from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.URLField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tease = models.TextField(null=True, blank=True)
    body = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'
        ordering = ['-date_created', ]

from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to='entries')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entires'

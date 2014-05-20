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
    status = models.IntegerField(choices=choices)

    date_created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        return ('entry_detail', [
            self.date_created.year,
            self.date_created.month,
            self.date_created.day,
            self.slug,
        ])

    class Meta:
        verbose_name_plural = 'entries'
        ordering = ['-date_created', ]

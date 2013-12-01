from django.db import models


class BoardMember(models.Model):
    """A class to represent the board members / staff
    of a given humane society. Most contact info is optional,
    but the user *must* have a ``name``, an ``order``, and a ``title``.
    """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    photo = models.URLField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255)
    bio = models.TextField()
    order = models.IntegerField()

    class Meta:
        ordering = ['order', ]

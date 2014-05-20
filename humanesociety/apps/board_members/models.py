from django.db import models


class BoardMember(models.Model):
    """A class to represent the board members / staff
    of a given humane society. Most contact info is optional,
    but the user *must* have a ``name``, an ``order``, and a ``title``.
    """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='staff', max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, help_text="""
        e.g, (222) 222-1010
    """)
    bio = models.TextField()
    order = models.IntegerField()

    class Meta:
        ordering = ['order', ]
        verbose_name = 'Staff Member'
        verbose_name_plural = 'Staff Members'

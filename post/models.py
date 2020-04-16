from django.db import models
from django.conf import settings
from django.db.models import Q

# Create your models here.

# class PostQuerySet(models.QuerySet):
#     def search(self, query=None):
#         qs = self
#         if query is not None:
#             or_lookup = (Q(title__icontains=query) | 
#                          Q(description__icontains=query)|
#                          Q(slug__icontains=query)
#                         )
#             qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
#         return qs

# class PostManager(models.Manager):
#     def get_queryset(self):
#         return PostQuerySet(self.model, using=self._db)

#     def search(self, query=None):
#         return self.get_queryset().search(query=query)


class PostModel(models.Model):
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title               = models.CharField(max_length=120)
    description         = models.TextField(null=True, blank= True)
    slug                = models.SlugField(blank=True, unique=True)
    publish_date        = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
#    objects             = PostManager()

    def __str__(self):
        return self.title

class Post(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.artist +' - '+ self.album_title
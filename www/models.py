from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class www(models.Model):
    about = models.TextField()
    about_extended = models.TextField()
    title = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return '{0}'.format(self.title)

class Post(models.Model):
    title = models.CharField('Post Title',max_length=32, unique=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=True, auto_created=True)
    text = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey(User)

    class Meta:
        ordering = ('-date',)

    def __unicode__(self):
        return self.title
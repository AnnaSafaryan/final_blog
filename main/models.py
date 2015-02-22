from django.db import models


# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=25)
    text = models.TextField()
    when = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{} at {}'.format(self.header, self.when)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    text = models.TextField(max_length=3000)
    when = models.DateTimeField(auto_now=True)
    header = models.CharField(max_length=25, default='')

    def __unicode__(self):
        return u'Comment at {}'.format(self.when)
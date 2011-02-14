from datetime import datetime
from docutils.core import publish_parts
from django.db import models
from annoying.decorators import signals

class Tag(models.Model):
    label = models.CharField(max_length=100)

    def __unicode__(self):
        return self.label

    class Meta:
        ordering = ('label',)

class ActivePostManager(models.Manager):
    def active(self):
        return self.filter(draft=False)


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    about = models.TextField(blank=True)
    about_html = models.TextField(blank=True)
    content = models.TextField(blank=True)
    content_html = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
    draft = models.BooleanField(default=True)
    created = models.DateTimeField(blank=True)

    objects = ActivePostManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-created',)

    @models.permalink
    def get_absolute_url(self):
        return ('post', None, {'slug': self.slug})


@signals.pre_save(sender=Post)
def refresh_html(sender, instance, **kwargs):
    instance.about_html = publish_parts(source=instance.about, writer_name="html4css1")['body']
    instance.content_html = publish_parts(
        source=instance.content,
        writer_name="html4css1",
        settings_overrides={'initial_header_level': 3},
    )['body']

    if instance.created:
        if not instance.draft and Post.objects.get(pk=instance.pk).draft:
            #going public
            instance.created = datetime.now()
    else:
        #a new object
        instance.created = datetime.now()

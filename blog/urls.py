from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
from blog.models import Post
from blog.views import FeedAll, FeedByTag

urlpatterns = patterns('',
    ('^$',
        'django.views.generic.simple.direct_to_template', {
            'template': 'blog/home.html',
            'extra_context': {
                'posts': Post.objects.active,
                'feed': lambda: reverse('feed'),
            },
        },
        'home',
    ),
    ('^tag/(?P<tag>.*)/feed/$',
        FeedByTag(),
        {},
        'feed_by_tag',
    ),
    ('^tag/(?P<tag>.*)/$',
        'blog.views.by_tag',
        {},
        'by_tag',
    ),
    ('^feed/$',
        FeedAll(),
        {},
        'feed',
    ),
    ('^(?P<slug>.*)/$',
        'blog.views.post',
        {},
        'post',
    ),
)

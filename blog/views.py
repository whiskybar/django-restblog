from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.syndication.views import Feed
from annoying.decorators import render_to
from annoying.functions import get_config
from blog.models import Post

@render_to('blog/home.html')
def by_tag(request, tag):
    return {
        'posts': Post.objects.active().filter(tags__label=tag),
        'feed': reverse('feed_by_tag', kwargs={'tag': tag}),
    }

@render_to('blog/post.html')
def post(request, slug):
    return {'post': get_object_or_404(Post, slug=slug)}


class FeedAll(Feed):
    title = get_config('FEED_TITLE', 'my blog')
    link = '/'
    description = get_config('FEED_DESCRIPTION', 'my ideas')

    def items(self):
        return Post.objects.active()[:settings.FEED_COUNT]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.about


class FeedByTag(FeedAll):
    def get_object(self, request, tag):
        return tag

    def title(self, tag):
        return '%s on %s' % (get_config('FEED_TITLE', 'my blog'), tag)

    def description(self, tag):
        return '%s on %s' % (get_config('FEED_DESCRIPTION', 'my ideas'), tag)

    def items(self, tag):
        return Post.objects.active().filter(tags__label=tag)[:get_config('FEED_COUNT', 5)]

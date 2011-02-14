Blog engine powered by reST
===========================

django-restblog is a very simple Django app for your blog. Write your blog
posts in `reStructuredText <http://docutils.sourceforge.net/rst.html>`_!


Features
--------

* Use reST both for the article preview and the article content.
* Caching the rendered HTML content.
* Draft (unpublished yet) articles.
* Tagging articles.
* RSS feeds for the main page and the articles by tag.


Installation
------------

Install from github using ``pip``::

    pip install -e git+git://github.com/whiskybar/django-restblog#egg=django-restblog

django-restblog uses `django-annoying <http://bitbucket.org/offline/django-annoying>`_::

    pip install -e hg+http://bitbucket.org/offline/django-annoying#egg=django-annoying

Last, you will need to make sure ``docutils`` is installed. Use your package 
manager or install the current version, like this::

    pip install docutils

Configuration
-------------

Add ``'blog'`` to your ``INSTALLED_APPS`` in ``settings.py`` of your project::

    INSTALLED_APPS = (
        ...
        'blog',
    )

Include the blog's URLs in your url config, like this::

    urlpatterns = patterns('',
        ...
        (r'', include('blog.urls')),
    )

Customize your blog feed with three constants in your ``settings.py``:

* ``FEED_COUNT`` (number of articles in the feed)
* ``FEED_TITLE``
* ``FEED_DESCRIPTION``

Do not forget to run ``syncdb`` to create the corresponding tables.


Usage
-----

You will need to provide the following two templates in your project:

* ``blog/home.html``: this is your homepage. It will list all your blog posts
  with their titles and their previews. There is no pagination yet. You can use
  the following template fragment for example::

    {% for post in posts %}
    <div class="post">
            <div class="title">
            <h2><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h2>
            <p>Posted on {{ post.created|date:"F j, Y" }}</p>
            </div>
    
            <div class="entry">
                {{ post.about_html|safe }}
            </div>
         
            <p class="footer">{% for tag in post.tags.all %}<a href="{% url by_tag tag %}">{{ tag }}</a>{% if not forloop.last %}, {% endif %}{% endfor %}</p>
    </div>
    {% endfor %}


* ``blog/post.html``: this is a post detail -- its content. For example::

    <div class="post">
        <div class="title">
        <h2><a href="{% url post post.slug %}">{{ post.title }}</a></h2>
        <p>Posted on {{ post.created|date:"F j, Y" }}</p>
        </div>

        <div class="entry">
            {{ post.content_html|safe }}
        </div>
     
        <p class="footer">{% for tag in post.tags.all %}<a href="{% url by_tag tag %}">{{ tag }}</a>{% if not forloop.last %}, {% endif %}{% endfor %}</p>
    </div>

For a complete example, see `the source of the blog lurkingideas.net <http://github.com/whiskybar/lurkingideas.net>`_.

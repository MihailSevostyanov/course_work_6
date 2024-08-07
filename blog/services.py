from django.core.cache import cache

from blog.models import Blog
from config import settings


def get_cached_blog_list(recached: bool = False):
    if settings.CACHE_ENABLED:
        print('get_cached_article_list')
        key = f'article_list'
        if recached:
            article_list = Blog.objects.all()
            cache.set(key, article_list)
        else:
            article_list = cache.get(key)
            if article_list is None:
                article_list = Blog.objects.all()
                cache.set(key, article_list)
    else:
        article_list = Blog.objects.all()
    return article_list
from django.http import HttpRequest

from .models import Category, Post
from .apps import BlogConfig


def blog_conf(request: HttpRequest):
    first_level_categories = Category.objects.filter(parent=None)
    try:
        about = Post.objects.get(slug='about')
    except Post.DoesNotExist:
        about = None
    return {
        'blog_conf': BlogConfig.blog_settings,
        'categories': first_level_categories,
        'about': about,
    }

from django.http import HttpRequest

from .models import Category, Post
from .apps import BlogConfig
from .views import has_permission_access_post


def blog_conf(req: HttpRequest):
    first_level_categories = Category.objects.filter(parent=None)
    try:
        about = Post.objects.get(slug='about')
        if not has_permission_access_post(req.user, about):
            about = None
    except Post.DoesNotExist:
        about = None
    return {
        'blog_conf': BlogConfig.blog_settings,
        'categories': first_level_categories,
        'about': about,
    }

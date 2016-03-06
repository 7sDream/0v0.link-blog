from django.http import HttpRequest

from .models import Category
from .apps import BlogConfig


def blog_conf(request: HttpRequest):
    first_level_categories = Category.objects.filter(parent=None)
    return {
        'blog_conf': BlogConfig.blog_settings,
        'categories': first_level_categories,
    }

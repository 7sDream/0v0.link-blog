import math

from django.http import HttpResponse, HttpRequest, Http404
from django.core.urlresolvers import reverse
from django.db.models import Q, F
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Tag, Category, Comment
from .apps import BlogConfig
from .forms import SearchFrom

Conf = BlogConfig.blog_settings


def get_item_in_page_or_404(the_list: list, page: str):
    try:
        page = int(page)
    except ValueError:
        raise Http404()

    if page <= 0:
        raise Http404()

    list_length = len(the_list)

    max_page_number = math.ceil(list_length / Conf['post_per_page'])
    max_page_number = 1 if max_page_number == 0 else max_page_number

    if page > max_page_number:
        raise Http404()

    start = Conf['post_per_page'] * (page - 1)
    end = start + Conf['post_per_page']

    return the_list.order_by('-pub_date')[start:end], page, max_page_number


def filter_post_list_by_user(the_list, user):
    if user.is_authenticated():  # is user
        if user.is_superuser:  # is Su
            return the_list
        elif user.author:  # is an author
            return the_list.exclude(Q(isDraft=True), ~Q(author=user.author))
        else:  # normal user
            return the_list.exclude(isDraft=True)
    else:
        return the_list.exclude(isDraft=True)


def has_permission_access_post(user, the_post):
    if not the_post.isDraft:
        return True
    if user.is_authenticated():
        if user.is_superuser:
            return True
        if user is the_post.author:
            return True
    return False


def index(req: HttpRequest, page: str = '1') -> HttpResponse:
    post_list = filter_post_list_by_user(Post.objects.all(), req.user)
    post_list, page, max_page = get_item_in_page_or_404(post_list, page)
    tags = Tag.objects.all()
    return render(req, 'blog/index.html', {
        'page': page,
        'max_page': max_page,
        'posts': post_list,
        'tags': tags
    })


def post(req: HttpRequest, slug: str) -> HttpResponse:
    the_post = get_object_or_404(Post, slug=slug)
    user = req.user

    if has_permission_access_post(user, the_post):
        the_post.view_times = F('view_times') + 1
        the_post.save()
        the_post.refresh_from_db()
        return render(req, 'blog/post.html', {
            'post': the_post,
        })

    raise Http404()


def category(req: HttpRequest, slug: str, page: str = '1') -> HttpResponse:
    the_category = get_object_or_404(Category, slug=slug)

    post_list = filter_post_list_by_user(
        Post.objects.filter(category__slug=slug), req.user)
    post_list, page, max_page = get_item_in_page_or_404(post_list, page)

    return render(req, 'blog/category.html', {
        'category': the_category,
        'posts': post_list,
        'page': page,
        'max_page': max_page,
        'tags': Tag.objects.all(),
    })


def tag(req: HttpRequest, slug: str, page: str = '1') -> HttpResponse:
    the_tag = get_object_or_404(Tag, slug=slug)

    post_list = filter_post_list_by_user(
        Post.objects.filter(tags__slug__contains=slug), req.user)
    post_list, page, max_page = get_item_in_page_or_404(post_list, page)

    return render(req, 'blog/tag.html', {
        'tags': Tag.objects.all(),
        'tag': the_tag,
        'posts': post_list,
        'page': page,
        'max_page': max_page,
    })


def search(req: HttpRequest):

    if req.method == 'GET':
        form = SearchFrom(req.GET, auto_id='%s')
        if form.is_valid():
            page = req.GET.get('page', '1')
            posts = Post.objects.filter(Q(title__contains=form.cleaned_data['keyword']) |
                                        Q(content__contains=form.cleaned_data['keyword']))
            posts = filter_post_list_by_user(posts, req.user)
            result_amount = len(posts)
            posts, page, max_page = get_item_in_page_or_404(posts, page)

            return render(req, 'blog/search.html', {
                'posts': posts,
                'keyword': form.cleaned_data['keyword'],
                'page': page,
                'max_page': max_page,
                'result_amount': result_amount,
            })
        else:
            return HttpResponse('参数填的不对不能搜哒！')


def share(req: HttpRequest, slug: str):
    the_post = get_object_or_404(Post, slug=slug)
    the_post.share_times = F('share_times') + 1
    the_post.save()
    post_url = req.build_absolute_uri(
        reverse('blog:post', kwargs={
            'slug': the_post.slug,
        }))
    url = 'http://www.jiathis.com/send/' \
          '?webid=tsina&url={0}&title=分享@7sDream 的文章：{1}'.format(
            post_url,
            the_post.title)

    return redirect(url)

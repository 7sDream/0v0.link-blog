from django.db import models
from django.contrib.auth.models import User

TAG_MAX_LENGTH = 20
CATEGORY_MAX_LENGTH = 40
NICKNAME_MAX_LENGTH = 40
TITLE_MAX_LENGTH = 50
REASON_MAX_LENGTH = 255

CN_TO_EN_RADIO = 2


class Tag(models.Model):
    name = models.CharField(max_length=TAG_MAX_LENGTH)
    slug = models.SlugField(max_length=TAG_MAX_LENGTH * CN_TO_EN_RADIO)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=CATEGORY_MAX_LENGTH)
    slug = models.SlugField(max_length=CATEGORY_MAX_LENGTH * CN_TO_EN_RADIO)
    parent = models.ForeignKey('self', null=True, blank=True,related_name='children')

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=NICKNAME_MAX_LENGTH)
    sign = models.TextField()

    def __str__(self):
        return '{self.nickname}({self.id})'.format(self=self)


class Post(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    slug = models.SlugField(max_length=TITLE_MAX_LENGTH * CN_TO_EN_RADIO)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField('publish date', auto_now_add=True)
    last_mod = models.DateTimeField('last modify date', auto_now=True)
    isDraft = models.BooleanField(default=False)

    view_times = models.IntegerField(default=0)
    share_times = models.IntegerField(default=0)

    def __str__(self):
        return "{self.title} - {self.author.nickname}".format(self=self)


class Modification(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=REASON_MAX_LENGTH)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return "{self.reason} at {self.time}".format(self=self)


class Comment(models.Model):
    nickname = models.CharField(max_length=NICKNAME_MAX_LENGTH)
    email = models.EmailField()
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             default=None, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='children')

    def __str__(self):
        return '{self.nickname}: {self.content}'.format(self=self)

from django.contrib import admin

from .models import Post, Author, Tag, Category, Modification, Comment


class ModificationInline(admin.TabularInline):
    model = Modification
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'category',
        'pub_date',
    ]

    ordering = ('-pub_date',)

    fieldsets = [
        ('文章', {
            'fields': [
                'title',
                'author',
                'content',
            ],
        }),
        ('元数据', {
            'fields': [
                'slug',
                'isDraft'
            ]
        }),
        ('分类', {
            'fields': [
                'category',
                'tags',
            ],
        }),
    ]

    inlines = [
        ModificationInline
    ]


class PostThroughTagInline(admin.StackedInline):
    model = Post.tags.through
    extra = 0


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'nickname',
        'id'
    ]
    ordering = ('-id',)


class TagAdmin(admin.ModelAdmin):
    inlines = [
        PostThroughTagInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        PostInline
    ]


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'post',
                'parent'
            ],
        }),
        ('用户信息', {
            'fields': [
                'nickname',
                'email'
            ],
        }),
        ('内容', {
            'fields': [
                'content'
            ],
        }),
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)

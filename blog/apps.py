from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = "Blog"

    # Blog settings
    blog_settings = {
        'name': '7sDream Blog',
        'description': '一个用来写代码，泡妹子，吐槽以及思考的小空间',
        'post_per_page': 5,
        'self_infos': [
            {'name': 'Github', 'url': 'https://github.com/7sDream', 'icon': 'github'},
            {'name': 'Zhihu', 'url': 'https://www.zhihu.com/people/7sdream', 'icon': 'question-circle'},
            {'name': 'Weibo', 'url': 'http://weibo.com/didilover', 'icon': 'weibo'},
            {'name': 'Ask.me', 'url': 'https://ask.fm/i7sdream', 'icon': 'at'},
            {'name': 'Email', 'url': 'mailto:xixihaha.xiha@qq.com', 'icon': 'envelope'},
        ],
    }

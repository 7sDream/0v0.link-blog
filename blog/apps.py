from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = "Blog"

    # Blog settings
    blog_settings = {
        'name': '7sDream Blog',
        'description': '漆黑烈焰使、邪王真眼、中二病、黑历史、技术宅、萝莉控、老司机、etc',
        'owner_name': '7sDream',
        'owner_sign': 'Forward.forward...',
        'owner_avatar': 'blog/image/dark_master.png',
        'post_per_page': 5,
        'self_infos': [
            {'name': 'Github', 'url': 'https://github.com/7sDream', 'icon': 'github'},
            {'name': 'Zhihu', 'url': 'https://www.zhihu.com/people/7sdream', 'icon': 'question-circle'},
            {'name': 'Weibo', 'url': 'http://weibo.com/didilover', 'icon': 'weibo'},
            {'name': 'Ask.me', 'url': 'https://ask.fm/i7sdream', 'icon': 'at'},
            {'name': 'Email', 'url': 'mailto:xixihaha.xiha@qq.com', 'icon': 'envelope'},
        ],
    }

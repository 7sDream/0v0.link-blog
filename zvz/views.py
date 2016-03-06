from django.template import RequestContext
from django.shortcuts import render


def handler404(req_context: RequestContext):
    return render(req_context, '404.html', {
        'home_url': req_context.get_host(),
    }, status=404)

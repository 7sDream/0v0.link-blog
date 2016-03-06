from django.template import RequestContext
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def handler404(req_context: RequestContext):
    return render(req_context, '404.html', {
        'home_url': req_context.get_host(),
    }, status=404)


def githook(req: HttpRequest):
    with open('/tmp/githook.txt', 'a') as f:
        f.write(str(req.POST))
    return HttpResponse()
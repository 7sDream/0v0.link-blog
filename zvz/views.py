from django.template import RequestContext
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json


def handler404(req_context: RequestContext):
    return render(req_context, '404.html', {
        'home_url': req_context.get_host(),
    }, status=404)


@csrf_exempt
def githook(req: HttpRequest):
    assert isinstance(req.META, dict)
    ua = req.META.get('HTTP_USER_AGENT', '')
    sha1 = req.META.get('HTTP_X_Hub_Signature', '')

    if not ua.startswith('GitHub-Hookshot/'):
        raise Http404()

    try:
        payload = json.loads(req.read(), encoding='utf-8')
        return HttpResponse(json.dumps(payload))
    except Exception as e:
        return HttpResponse(str(e))

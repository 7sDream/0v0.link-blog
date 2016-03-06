from django.template import RequestContext
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json


def handler404(req_context: RequestContext):
    return render(req_context, '404.html', {
        'home_url': req_context.get_host(),
    }, status=404)


@csrf_exempt
def githook(req: HttpRequest):
    try:
        with open('/tmp/githook.txt', 'a') as f:
            f.write(str(json.loads(req.read().decode('utf-8'))))
        return HttpResponse()
    except Exception as e:
        return HttpResponse(str(e))

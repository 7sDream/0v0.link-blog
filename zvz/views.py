import os
import json
import hmac
import hashlib
import subprocess

from django.template import RequestContext
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static

from blog.models import GithubHookSecret


def handler404(req_context: RequestContext):
    return render(req_context, '404.html', {
        'home_url': req_context.get_host(),
    }, status=404)


@csrf_exempt
def githook(req: HttpRequest):

    # check User-agent
    if not req.META.get('HTTP_USER_AGENT', '').startswith('GitHub-Hookshot'):
        return HttpResponse('UA error')

    # check event
    if not req.META.get('HTTP_X_GITHUB_EVENT', '') == 'push':
        return HttpResponse('Event error')

    try:
        # check sha1 signature
        name, req_sha1 = req.META.get('HTTP_X_HUB_SIGNATURE', '').split('=')
        if name != 'sha1':
            return HttpResponse('Signature format error')
        HOOK_SECRET_KEY = get_object_or_404(GithubHookSecret, pk=1)
        data = req.read()
        mac = hmac.new(HOOK_SECRET_KEY.secret.encode(), data, digestmod=hashlib.sha1)
        if not hmac.compare_digest(mac.hexdigest(), req_sha1):
            return HttpResponse('Signature check error')

        # get payload
        payload = json.loads(data.decode('utf-8'), encoding='utf-8')

        # check branch
        if payload['ref'].endswith('master'):
            script = os.path.join(settings.BASE_DIR, 'deploy.sh')
            proc = subprocess.Popen([script], stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            return HttpResponse(proc.communicate()[0])
        else:
            return HttpResponse('Not master branch, ignore')
    except Exception as e:
        return HttpResponse(str(e))


def icon(req: HttpResponse):
    return redirect(static('blog/image/favicon.ico'))

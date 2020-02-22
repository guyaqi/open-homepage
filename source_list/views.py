import logging, os, json
from django.http import HttpResponse, JsonResponse
from source_list.models import OpenBlog

from source_list import util

# for debug use
def update(r):
  util.update()
  return HttpResponse('ok')

def get(r):
  v = util.all_sources()
  return HttpResponse(json.dumps(v))
from django.http import HttpResponse, JsonResponse
from source_list import util as source_util
from open_api import util as api_util
import json

def all_blog(request):
  sources = source_util.all_sources()
  blogs = []

  for source in sources:
    if source['type'] == 'github':
      blogs += api_util.getBlogFromGithub(source)
  
  return HttpResponse(json.dumps(blogs))

def all_source(request):
  sources = source_util.all_sources_with_index()
  
  return HttpResponse(json.dumps(sources))
from django.http import HttpResponse, JsonResponse
from source_list import util as source_util
from open_api import util as api_util
from source_list.models import OpenBlog
import json, requests

def all_blog(request):
  sources = source_util.all_sources()
  blogs = []

  for source in sources:
    if source['type'] == 'github':
      blogs += api_util.getBlogFromGithub(source)
  
  return HttpResponse(json.dumps(blogs))

def blog_by_id(request, source_id):
  qs = OpenBlog.objects.filter(blog_id=source_id)
  if len(qs) == 0:
    return HttpResponse(json.dumps([]))
  the_source = qs[0]
  blogs = api_util.getBlogFromGithub(the_source)
  return HttpResponse(json.dumps(blogs))


def all_source(request):
  sources = source_util.all_sources_with_index()
  
  return HttpResponse(json.dumps(sources))

def blog_by_id_id(request, source_id, blog_id):
  qs = OpenBlog.objects.filter(blog_id=source_id)
  if len(qs) == 0:
    return HttpResponse(json.dumps([]))
  the_source = qs[0]
  blogs = api_util.getBlogFromGithub(the_source)
  try:
    the_blog = blogs[blog_id]
  except IndexError as e:
    return HttpResponse('blog not found')
  
  try:
    res = requests.get(the_blog)
    res = res.text()
    return HttpResponse(res)
  except Exception as e:
    return HttpResponse('get blog failed')

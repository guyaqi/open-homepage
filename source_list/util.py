import logging, os, json
from open_homepage.settings import BASE_DIR
from source_list.models import OpenBlog

logging.basicConfig(
  level = logging.INFO,
  format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def update():
  SOURCE_LIST = os.path.join(BASE_DIR, 'sources')
  logger.info(f'源列表 {SOURCE_LIST}')

  qs = OpenBlog.objects.all()
  for item in qs:
    item.delete()

  for root,dirs,files in os.walk(SOURCE_LIST):
    for file in files:
      full_path = os.path.join(root,file)
      conf = open(full_path, 'r', encoding='utf8')
      conf_name = file.split('.')[0]
      conf = conf.read()

      logger.info(f'读取 {conf_name}')
      newBlog = OpenBlog()
      newBlog.blog_info = conf
      newBlog.save()

def all_sources():
  qs = OpenBlog.objects.all()
  v = []
  for item in qs:
    v.append(json.loads(item.blog_info))
  
  return v
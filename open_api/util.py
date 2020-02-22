import requests
import yaml

def getBlogFromGithub(info):

  # 仓库是否在使用
  using = info.get('use')
  if using is None:
    using = True
  
  if not using:
    return []

  name = info.get('repo')
  if name is None:
    print('repo name missed')
    return []
  
  # 获取分支
  branch = info.get('branch')
  if branch is None:
    branch = 'master'

  # openfile位置
  openfile = info.get('openfile')
  if openfile is None:
    openfile = 'open.yml'
  
  openfile_full_path = f'https://raw.githubusercontent.com/{name}/{branch}/{openfile}'
  # print(openfile_full_path)
  # https://raw.githubusercontent.com/guyaqi/openBlogEx1/master/open.yml

  try:
    res = requests.get(openfile_full_path)
    res = res.text
    open_rule = yaml.load(res)
  except Exception as e:
    print(f'{openfile_full_path} 读取失败')
    return []
  file_names = []
  for one in open_rule['blogs']:
    file_names.append(f'https://raw.githubusercontent.com/{name}/{branch}/{one}')

  return file_names
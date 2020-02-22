from django.db import models

# Create your models here.
class OpenBlog(models.Model):
  blog_id = models.AutoField(primary_key=True)
  blog_info = models.CharField(default='github', max_length=512)
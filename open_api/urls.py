from django.urls import path
from open_api import views

urlpatterns = [
    path('all_blog', views.all_blog),
    path('blog/<source_id:int>', views.blog_by_id),
    path('all_source', views.all_source),
    
]
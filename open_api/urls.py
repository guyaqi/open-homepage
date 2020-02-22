from django.urls import path
from open_api import views

urlpatterns = [
    path('all_blog', views.all_blog),
    path('blog/<int:source_id>', views.blog_by_id),
    path('all_source', views.all_source),
    path('blog/<int:source_id>/<int:blog_id>', views.blog_by_id_id),
    
]
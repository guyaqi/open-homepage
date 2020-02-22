from django.urls import path
from open_api import views

urlpatterns = [
    path('all_blog', views.all_blog),
    path('all_source', views.all_source),
    
]
from django.urls import path
from open_api import views

urlpatterns = [
    path('all_blog', views.all_blog),
]
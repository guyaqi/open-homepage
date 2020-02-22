from django.urls import path
from source_list import views

urlpatterns = [
    path('update', views.update),
    path('get', views.get),
]
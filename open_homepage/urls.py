
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('source_list/', include('source_list.urls')),
    path('open_api/', include('open_api.urls')),
]

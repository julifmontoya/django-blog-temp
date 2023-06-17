from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve 
from django.urls import re_path
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),   
]
urlpatterns += [
    re_path(r'^favicon\.ico$',RedirectView.as_view(url='https://en.wikipedia.org/wiki/Favicon#/media/File:Etsy_icon.svg')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

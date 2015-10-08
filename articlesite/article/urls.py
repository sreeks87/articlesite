from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static 
'''
url patters for the webapp
'''
urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^category/(?P<cat>[a-zA-Z]+)/$', views.article_cat_fetch, name='article_cat_fetch')
]
'''
Checking for development env, if dev env then appending the static and media 
root to serve the files from.
'''
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
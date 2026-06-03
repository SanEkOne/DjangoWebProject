from django.urls import include, path
from .views import main_page, news_page, management_page, about_page, contacts_page
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', main_page, name='main'),
    path('admin/', admin.site.urls),

    path('news/', include('News.urls')),
    path('management/', include('Management.urls')),
    path('store/', include('Store.urls')),
      
    path('about/', about_page, name='about'),
    path('contacts/', contacts_page, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'django.views.defaults.page_not_found'

# from django.conf import settings  # импорты чтобы css работал при DEBUG=False
# from django.conf.urls.static import static
# from django.views.static import serve
# from django.urls import re_path

# if not settings.DEBUG:  #чтобы css работал при DEBUG=False
#     urlpatterns += [
#         re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
#     ]
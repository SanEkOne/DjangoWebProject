from django.urls import include, path
from .views import main_page, news_page, management_page, about_page, contacts_page

urlpatterns = [
    path('', main_page, name='main'),

    path('news/', include('News.urls')),
    path('management/', include('Management.urls')),
      
    path('management/', management_page, name='management'),
    path('about/', about_page, name='about'),
    path('contacts/', contacts_page, name='contacts'),
]
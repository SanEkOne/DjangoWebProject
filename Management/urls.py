# from django.urls import path
# from . import views

# app_name = 'management_app'

# urlpatterns = [
#     path('', views.index, name='index'),
# ]


from django.urls import path
from .views import IndexView 

app_name = 'management_app' 

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
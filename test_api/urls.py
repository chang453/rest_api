"""test_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
import rest_framework
from django.conf import settings
from django.conf.urls.static import static
from test_app.views import *
from django.conf.urls import url, include



urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    path('', api_view.as_view(), name = 'API_view'),
    path('api_list', api_view.as_view(), name = 'API_list_view'),
    path('api_list/<no>', api_detail_view.as_view(), name = 'API_detail'),
    path('api_list/<no>/update', api_update_view.as_view(), name = 'API_update'),
    path('api_list/<no>/delete', api_delete_view.as_view(), name = 'API_delete'),
    path('api_list/create', api_create_view.as_view(), name = 'API_create')
]

# urlpatterns = [
#     url('api-auth/', include('rest_framework.urls')),
#     url(r'^$', api_view.as_view(), name = 'API_view'),
#     url(r'^api_list$', api_view.as_view(), name = 'API_list_view'),
#     url(r'^api_list/(?P<no>\d+)$', api_detail_view.as_view(), name = 'API_detail'),
#     url(r'^api_list/(?P<no>\d+)/update$', api_update_view.as_view(), name = 'API_update'),
#     url(r'^api_list/(?P<no>\d+)/delete$', api_delete_view.as_view(), name = 'API_delete'),
#     url(r'^api_list/create$', api_create_view.as_view(), name = 'API_create')
# ]



app_name = 'test_api'

# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'todo_board', tsrm)
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


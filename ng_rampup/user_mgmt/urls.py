__author__ = 'ubuntu'

from django.conf.urls import patterns, url
from user_mgmt.views import LoginView, UserViewSet, LogoutView
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
urlpatterns = patterns('',
                       url(r'^$', LoginView.as_view(), name='login'),
                       url(r'^logout$', LogoutView.as_view(), name='logout')
                       )
urlpatterns += router.urls
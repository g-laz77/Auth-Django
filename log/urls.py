#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$',views.about),
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
]

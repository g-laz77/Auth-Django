
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from log.forms import LoginForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('log.urls')),
    url(r'^login/$', views.login,{'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^home/$', views.login,{'template_name': 'home.html'}),
    url(r'^logout/$', views.logout, {'next_page': '/login/'}),
]
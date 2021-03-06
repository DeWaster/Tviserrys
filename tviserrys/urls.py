from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, include, url
from django.conf.urls import url
from django.contrib import admin
from . import views
from tviserrys.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/', views.RegisterView.as_view(), name='register'),
    url(r'^tviit/', include('tviit.urls', namespace='tviit')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^password_change/$', auth_views.password_change),
    url(r'^password_change/done/$', auth_views.password_change_done),
    url(r'^password_reset/$', auth_views.password_reset),
    url(r'^password_reset/done/$', auth_views.password_reset_done),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm),
    url(r'^reset/done/$', auth_views.password_reset_complete),
    url(r'^profile/', include('user_profile.urls', namespace='profile')),
    url(r'^search/', include('haystack.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT, 'show_indexes': False}),
]

urlpatterns += patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
)

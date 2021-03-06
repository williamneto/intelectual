from django.conf.urls.defaults import *

urlpatterns = patterns('intelectual.accounts.fviews',
                       url(r'^login/$', 'login'),
                       url(r'^logout/$', 'logout_then_login'),
                       url(r'^password_change/$', 'password_change'),
                       url(r'^password_change/done/$', 'password_change_done'),
                       url(r'^password_reset/$', 'password_reset'),
                       url(r'^password_reset/done/$', 'password_reset_done'),
                       url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,20})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$','password_reset_confirm'),
                       url(r'^reset/done/$',
                           'password_reset_complete'),
)


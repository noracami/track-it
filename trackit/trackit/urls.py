from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trackit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'issues.views.home', name='home'),

    url(r'^issues/(?P<ticket_id>\d+)/$', 'issues.views.issues', name='issues'),
    url(r'^issues/new/$', 'issues.views.newissues', name='newissues'),
    url(r'^tags/new/$', 'issues.views.newlabels', name='newlabels'),
    url(r'^add/$', 'issues.views.add', name='add'),
    url(r'^edit/$', 'issues.views.edit', name='edit'),
    url(r'^change_status/$', 'issues.views.change_status', name='change_status'),
    url(r'^users/$', 'issues.views.users', name='users'),
    url(r'^users/(?P<user_id>\d+)/$', 'issues.views.users', name='users'),
    url(r'^users/new/$', 'issues.views.newusers', name='newusers'),
    url(r'^loginhere/$', 'issues.views.loginhere', name='loginhere'),
    url(r'^login/$', 'issues.views.login', name='login'),
    url(r'^logout/$', 'issues.views.logout', name='logout'),
    url(r'^error/loginhere/$', 'issues.views.loginhere', name='errorinloginhere'),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'hoh.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^createuser/$','users.views.userLogin'),
    url(r'^checkin/$','helpreq.views.checkIn'),
    url(r'^help/$','helpreq.views.help'),
    url(r'^test/$','testhoh.views.test'),
    url(r'^getmap/$','heatmap.views.getlats')
]
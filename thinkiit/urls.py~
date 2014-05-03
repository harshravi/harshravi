from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from home.views import *
from support.views import *
from upload.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thinkiit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$',home),
    url(r'^$',home),
    url(r'^notes/$',jee),
    url(r'^login$',login),
    url(r'^signup$',signup),
    url(r'^jee$',jee),
    url(r'^google_search$',search),
    url(r'^display$',ua_display),
    url(r'^support$',ua_display),
    url(r'^upload$',upload),
    url(r'^admins$',admins),
    url(r'^adminji$',adminji),
    url(r'^user$',user),
    url(r'^video$',video),
    url(r'^search/$',search),
    url(r'^phy_index/$',phy_index),
    url(r'^chem_index/$',chem_index),
    url(r'^maths_index/$',maths_index),
    url(r'^lecture_index/$',lecture_index),
    url(r'^test/$',test),
    url(r'^class/$',classes),
    url(r'^solution/$',solution),
    url(r'^contact/',contact),
    url(r'^about_us/',about_us),
    url(r'^term_cond/',term_cond),
    url(r'^cancellation_return/',cancellation_return),
    url(r'^privacy_policy/',privacy_policy),
    url(r'^branch_selector/',branch_selector),
)

urlpatterns += staticfiles_urlpatterns()

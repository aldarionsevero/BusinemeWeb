from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'BusinemeWeb.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^cadastro/',
                           'controllers.user.register_user_page'),
                       url(r'^cadastrar/usuario',
                           'controllers.user.register_user'),
                       url(r'^home/', 'controllers.home.home'),
                       url(r'^admin/', include(admin.site.urls)),
                       )

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'BusinemeWeb.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^cadastro/',
                           'controllers.user.register_user_page'),
                       url(r'^$',
                           'controllers.app.feed_page'),
                       url(r'^cadastrar/usuario',
                           'controllers.user.register_user'),
                       url(r'^logar/usuario',
                           'controllers.user.log_user'),
                       url(r'^login/', 'controllers.app.login'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^perfil/', 'controllers.user.user_account'),
                       url(r'^perfil/sair/', 'controllers.user.logout_user'),
                       url(r'^perfil/alterar_dados/',
                           'controllers.user.change_userdata'),
                       # /\ Url for the
                       # current try to change the user data
                       )

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
                       url(r'^cadastrar/usuario/$',
                           'controllers.user.register_user'),
                       url(r'^login/', 'controllers.user.log_user'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^perfil/', 'controllers.user.user_account'),
                       url(r'^alterarcao_senha/',
                           'controllers.user.change_password_page'),
                       url(r'^alterar_senha/',
                           'controllers.user.change_password'),
                       url(r'^sair/', 'controllers.user.logout_user'),
                       url(r'^alterar_dados/',
                           'controllers.user.change_userdata'),
                       url(r'^exclusao_perfil/',
                           'controllers.user.delete_account_page'),
                       url(r'^excluir_perfil/',
                           'controllers.user.delete_account'),
                       )

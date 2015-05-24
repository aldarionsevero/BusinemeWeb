from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'BusinemeWeb.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^cadastro/',
                           'controllers.userController.register_user_page'),
                       url(r'^$',
                           'controllers.app.feed_page'),
                       url(r'^cadastrar/usuario/$',
                           'controllers.userController.register_user'),
                       url(r'^login/', 'controllers.userController.log_user'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^perfil/',
                           'controllers.userController.user_account'),
                       url(r'^alterarcao_senha/',
                           'controllers.userController.change_password_page'),
                       url(r'^alterar_senha/',
                           'controllers.userController.change_password'),
                       url(r'^sair/',
                           'controllers.userController.logout_user'),
                       url(r'^alterar_dados/',
                           'controllers.userController.change_userdata'),
                       url(r'^desativacao_perfil/',
                           'controllers.userController.deactivate_account_page'),
                       url(r'^desativar_perfil/',
                           'controllers.userController.deactivate_account'),
                       url(r'^buscar_linha/',
                           'controllers.busline_controller.search_line'),
                       url(r'^busca_avancada/',
                           'controllers.busline_controller.advanced_search_line'),
                       url(r'^busca_avancada_page/',
                           'controllers.busline_controller.advanced_search_page'),
                       )

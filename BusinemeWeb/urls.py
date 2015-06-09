from django.conf.urls import patterns, include, url
from django.contrib import admin
from controllers import post_controller

urlpatterns = patterns(
    '',
    url(r'^cadastro/',
        'controllers.user_controller.register_user_page'),
    url(r'^$',
        'controllers.app.feed_page'),
    url(r'^cadastrar/usuario/$',
        'controllers.user_controller.register_user'),
    url(r'^login/', 'controllers.user_controller.log_user'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^perfil/',
        'controllers.user_controller.user_account_page'),
    url(r'^alterar_senha/',
        'controllers.user_controller.change_password'),
    url(r'^sair/',
        'controllers.user_controller.logout_user'),
    url(r'^alterar_dados/',
        'controllers.user_controller.change_userdata'),
    url(r'^desativar_perfil/',
        'controllers.user_controller.deactivate_account'),
    url(r'^buscar_linha/',
        'controllers.busline_controller.search_line'),
    url(r'^resultado/busca_avancada/',
        'controllers.busline_controller.advanced_search_busline'),
    url(r'^busca_avancada/',
        'controllers.busline_controller.advanced_search_busline_page'),
    url(r'^realizar_post/',
        post_controller.make_post),
)

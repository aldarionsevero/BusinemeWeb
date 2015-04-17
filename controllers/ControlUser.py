from user import User
# Classe validadora


class ControlUser():

    # def validaNome(nome):

        # Cadastra usuario
    def save_user(self, request):  # recebe requisicao que vem da pagina
        new_user = User()

        # Escrevendo novo user
        # coloca o campo nome no atributo nome do usuário
        new_user.name = request.POST["nome"]
        new_user.password = request.POST["password"]  # ||
        new_user.email = request.POST["email"] 		# ||
        new_user.userName = request.POST["userName"]  # ||
        new_user.save()

    # (? request ou resource) metodo para abrir paginas do formulario
    # def callForm(request):

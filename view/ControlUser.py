from user import User
#Classe validadora


class ControlUser():

	def validaNome(nome):
		



	#Cadastra usuario
	def saveUser(request):  #recebe requisicao que vem da pagina
		newUser = User()

		# Escrevendo novo user
		newUser.name = request.POST["nome"]  		#coloca o campo nome no atributo nome do usuário
		newUser.password = request.POST["password"] # ||
		newUser.email = request.POST["email"] 		# ||
		newUser.userName = request.POST["userName"] # ||
		newUser.save()

	def callForm(request):  # (? request ou resource) metodo para abrir paginas do formulario
		
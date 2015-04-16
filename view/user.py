from django.db import models

class User(models.Model):
	"""docstring for User"""

	name = models.CharField(max_lenght = 200) #Definir uma constante para esse valor
	password = models.CharField(min_lenght = 8 , max_lenght = 15) #Definir uma constante para max e min de senha
	email = models.CharField(max_lenght = 50,blank = false) #Definir uma constante para maxEmail. blank = false nao perminte entrada em branco
	userName = models.CharField(max_lenght = 20) # ||






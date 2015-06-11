Feature: Make a post.
	To Make a post
	As an user	
	I want to make a post about a busline using some informations

	Scenario: I fill the field "busline"
	    Given I am on Busine.me homepage
        And I type "205" in the field "busline"
        When I press "Pesquisar"
	    Then I should see "Businar!"

	Scenario: I press the button "Businar!" on "busline_profile.html"
		Given I am on Busine.me homepage
		And I type "205" in the field "busline"
		And I press "Pesquisar"
		And I follow "/perfil_de_linha/0.205/"  
		Then I should see "Informações"      

	Scenario: I press the button "Businar!" without sign in
		Given I am on Busine.me homepage
		And I type "205" in the field "busline"
		And I press "Pesquisar"
		And I press "Businar!" 
		Then I should see "Erro :("


	Scenario: I press the button "Businar!" without sign in
		Given I am on Busine.me loginpage
		And I type "rapifire" in the field "username"
		And I type "123" in the field "password"
		And I press "Entrar"
		And I type "205" in the field "busline"
		And I press "Pesquisar"
		And I press "Businar!" 
		Then I should see "Realize uma Businada!"
Feature: Make a line sugestion.
    To Make a sugestion of line
    As an user  
    I want to make a line sugestion 

Scenario: I  load  the sugest line

	Scenario: I fill the field "busline"
	    Given I am on Busine.me homepage
        And I type "205" in the field "busline"
        When I press "Pesquisar"
	    Then I should see "sugerir linha-- buscaavancada"

	Scenario I dont fill  the field  
		Given I am on Busine.me homepage
        And I type "205" in the field "busline"
        And I press "Pesquisar"
		And I type "Leste" in the field "description"
		When I press"registrar sugestao de Linha"
		Then I should  see "preencha este campo" 

    Scenario 
		Given I am on Busine.me homepage
        And I type "205" in the field "busline"
        And I press "Pesquisar"
		And I type "Leste" in the field "description"
		When I press"registrar sugestao de Linha"
		Then I should  see "preencha este campo" 


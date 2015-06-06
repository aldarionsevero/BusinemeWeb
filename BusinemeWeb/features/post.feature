Feature: Make a post.
	To Make a post
	As an user	
	I want to make a post about a busline using some informations, like:

	Scenario: Do not modify any field
	    Given I am on Busine.me homepage
	    And I press "Busine"
	    And I press "Businar!"
	    Then I should see a message saying "Erro"

	Scenario: I fill the field "Linha"
	    Given I am on Busine.me homepage
	    And I press "Busine"
	    And I type "0.205" in the field "Linha"
	    And I type "Este ônibus é bonito" in the field "Comentário"
	    When I press "Businar!"
	    Then I should see "0.205 \n  Comentário: Este ônibus é bonito"

	Scenario: I press the button "Businar!"
		Given I am on Busine.me homepage
		And I type "205" in the field "busline"
		And I press "Pesquisar"
        When I press "Businar!"
        Then I should see "Realize uma Businada!"



	Scenario: I press the button "Businar!" on "realizar_post.html"
		Given I am on Busine.me homepage
		And I type "205" in the field "busline"
		And I press "Pesquisar"
        And I press "Businar!"
        When i press "Businar!"
        Then I should see "O que é o Busine.me?"





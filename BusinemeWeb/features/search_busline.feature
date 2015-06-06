Feature: Search busline
    In order to check a busline
    As an user
    I want to search for a busline

    Scenario: Search by line number
        Given I am on Busine.me homepage
        And I type "205" in the field "busline"
        When I press "Pesquisar"
        Then I should see "Resultado"
        And I should see a description saying "Foram encontradas '2' linhas" 

	Scenario: Search by line number
        Given I am on Busine.me homepage
        And I type "" in the field "busline"
        When I press "Pesquisar"
        Then I should see "Resultado"
        And I should see a description saying "Foram encontradas '1000' linhas" 



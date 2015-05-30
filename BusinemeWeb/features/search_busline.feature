Feature: Search busline
    In order to check a busline
    As an user
    I want to search for a busline

    Scenario: Search by line number
        Given I am on Busine.me home page
        And I type "205" in the field "busline"
        When I press "Pesquisar"
        Then I should see "Resultado"
        And I should see a description saying "Foram encontrados '2' linhas que possuem '205' em seus números." 


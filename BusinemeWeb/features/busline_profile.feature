Feature: Busline profile page
  To see about a busline
  As an user
  I want to see the information from the busline, like: 


  Scenario: I click on the number of busline in result page
        Given I am on Busine.me homepage
        And I type "205" in the field "busline"
        And I press "Pesquisar"
        When I press "0.205"
        Then I should see a message saying "Informações sobre a linha 0.205"
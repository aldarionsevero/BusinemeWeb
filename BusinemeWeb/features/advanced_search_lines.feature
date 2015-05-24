Feature: Advanced search of a busline
  To find a busline faster
  As an user
  I want to search for a busline with more filters
  
  Scenario: Do not fill any filter
    Given I am on Busine.me homepage
    And I go to "Advanced Search"
    When I press "Search"
    Then I should see "Entre com pelo menos um filtro utilizar a busca avançada"
    
  Scenario: I fill the filter field "via"
    Given I am on Busine.me homepage
    And I go to "Advanced Search"
    And I type "Gama" in the field "via"
    When I press "Search"
    Then I should see "Foram encontradas 'X' linhas que passam pelo 'Gama'"
    
  Scenario: I fill more than one filter field
    Given I am on Busine.me homepage
    And I go to "Advanced Search"
    And I type "Leste" in the field "via"
    And I type "205" in the field "busline"
    When I press "Search"
    Then I should see "Foram encontrada '1' linha(s) que passa(m) pelo 'Gama', com o número '205'"

Feature: Advanced search of a busline
  To find a busline faster
  As an user
  I want to search for a busline with more filters
  
  Scenario: Do not fill any filter
    Given I am on Busine.me homepage
    And I press "Pesquisar"
    And I follow "/busca_avancada/"
    When I press "Procurar"
    Then I should see a message saying "Erro"
    
  Scenario: I fill the filter field "via"
    Given I am on Busine.me homepage
    And I press "Pesquisar"
    And I follow "/busca_avancada/"
    And I type "Gama" in the field "description"
    When I press "Procurar"
    Then I should see a description saying "Foram encontradas '82' linhas"
    
  Scenario: I fill more than one filter field
    Given I am on Busine.me homepage
    And I press "Pesquisar"
    And I follow "/busca_avancada/"
    And I type "205" in the field "busline_advanced"
    And I type "Leste" in the field "description"
    When I press "Procurar"
    Then I should see a description saying "Foram encontradas '1' linhas"
    

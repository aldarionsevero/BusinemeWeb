Feature: Advanced search of a busline
  To find a busline faster
  As an user
  I want to search for a busline with more filters
  
  Scenario: Do not fill any filter
    Given I am on Busine.me homepage
    And I press "Pesquisar"
    And I press "Busca Avancada"
    When I press "Procurar"
    Then I should see a message saying "Erro"
    
  Scenario: I fill the filter field "via"
    Given I am on Busine.me homepage
    And I press "Pesquisar"
    And I press "Busca Avancada"
    And I type "Gama" in the field "description"
    When I press "Procurar"
    Then I should see "0.020 \n Rota: Santa Maria (Av. Santa Maria)/Gama Sul-Central-Oeste-Leste-Rodoviária \n VIA CONT. QR 218/318 - SANTA MARIA \n Percurso: 48.35 KM \n Tarifa: R$1.5"
    
  Scenario: I fill more than one filter field
    Given I am on Busine.me homepage
    And I press "Pesquisar"
    And I press "Busca Avancada"
    And I type "Leste" in the field "description"
    And I type "205" in the field "busline"
    When I press "Procurar"
    Then I should see "Foram encontrada '1' linha(s) que passa(m) pelo 'Gama', com o número '205'"

Feature: Favorite busline.
    To see my favorite buslines
    As an user
    I would like to favorite my favorite busline
   
   Scenario: I press the button "Favoritar"
        Given I am on Busine.me homepage
        And I type "205" in the field "busline"
        And I press "Favoritar"
        And I should see "205 adicionado aos favoritos"
        When I press "Favoritos"
        Then I should see "Businadas"


   

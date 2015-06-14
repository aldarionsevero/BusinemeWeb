Feature: Make a review.
    To Make a review
    As an user  
    I want to make a review about a previous post

Scenario: I review a previous post

        Given I am on Busine.me homepage
        And I type "205" in the field "busline"
        And I press "Pesquisar"
        When I press "Businar"
        Then I should see "Realize uma Businada"
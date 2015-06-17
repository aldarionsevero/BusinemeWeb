Feature: Make a review.
    To Make a review
    As an user  
    I want to make a review about a previous post

Scenario: I review a previous post

	Scenario: I fill the field "busline"
	    Given I am on Busine.me homepage
        And I type "205" in the field "busline"
        When I press "Pesquisar"
	    Then I should see "Businar!"
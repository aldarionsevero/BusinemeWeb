Feature: Search busline
    In order to check a busline
    As an user
    I want to search for a busline

    Scenario: Search by line number
        Given I am on Busine.me home page
        And I type "205" in the field search lines
        When I press "Search"
        Then I should see "Results"
        And I should see "We found '2' buslines that contains '205' in their numbers"
        And I should see the list with the found bulines.

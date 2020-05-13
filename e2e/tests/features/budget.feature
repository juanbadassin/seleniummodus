Feature: Budget app


#    Scenario Outline: Users should be able to add a new item
#        Given I navigate to the budget page
#        When I add a new item of type <item_type>
#        Then The item is added to the table
#
#        Examples: Item types
#        | item_type       |
#        | inflow          |
#        | outflow         |
#
#
#    Scenario: Total inflow is updated
#        Given I navigate to the budget page
#        And I save the current total inflow amount
#        When I add a new item of type inflow
#        Then The total inflow is correctly increased
#
#
#    Scenario: Total outflow is updated
#        Given I navigate to the budget page
#        And I save the current total outflow amount
#        When I add a new item of type outflow
#        Then The total outflow is correctly decreased


    Scenario: Only values different from zero are allowed
        Given I navigate to the budget page
        And I count the amount of items in the table
        When I add a new item with 0 value
        Then The amount of items has not change
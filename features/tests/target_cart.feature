# Created by ashish at 12/4/24
Feature: Test  Scenario for Cart Icon functionality
  # Enter feature description here

  Scenario: User gets the message for empty cart
    Given Open Target main page
    When User Clicks on cart icon
    Then Verify "Your Cart is empty" message is shown


# Created by ashish at 12/6/24
Feature: Test scenario for Sign-In page

  Scenario: User is able to sign-in on target account
    Given Open Target main page
    When User click on Sign-in button
    When User click on Sign in button on the navigation page on the right side
    Then Verify Sign-In Form is opened


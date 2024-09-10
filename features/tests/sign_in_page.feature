# Created by dang at 8/27/24
Feature: Reelly Sign In feature tests

  Scenario: User want to sign in with correct credentials
      Given Open Reelly wellcome page
      When Click Open in Browser
      And Enter email "**********" and "********"
      And Click Continue Button
      Then Verify user is logged in

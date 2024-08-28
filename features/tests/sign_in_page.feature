# Created by dang at 8/27/24
Feature: Reelly Sign In feature tests

  Scenario: User want to sign in with correct credentials
      Given Open Reelly main page
      When Click Open in Browser
      And Enter email "antonov.resu@gmail.com" and "Internship2024!"
      And Click Continue Button
      Then Verify user is logged in

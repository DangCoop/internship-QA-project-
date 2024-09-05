# Created by dang at 8/28/24
Feature: Off Plan Page UI testing

  Scenario Outline: User can filter the off plan products by Unit price range
    Given Open Reelly wellcome page
    When Click Open in Browser
    And Enter email <email> and <password>
    And Click Continue Button
    And Verify the right page opens
    Then Open filter menu
    And Filter the products by price range from <price1> to <price2> AED
    And Apply Filter
    And Verify the price in all cards is inside the range (1200000 - 2000000)
    Examples:
      | email                    | password          | price1  | price2  |
      | "*********" | "**********" | 1200000 | 2000000 |
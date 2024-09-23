@regressionTest

Feature: Automated the open cart page

    Scenario Outline: The user get product and purchase
      Given user open browser
      And user go to the register page
      When user register in the page
      Then the user registers successfully
      And search the product "<product>" and select it
      When add to cart "<quantity>" product
      And go to checkout
      And fill the checkout form "<country>" "<state>"
      Then the user purchase the product

    Examples:
      |product|quantity|country |state    |
      |IMAC   |2       |Colombia|Antioquia|

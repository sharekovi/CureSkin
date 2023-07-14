
Feature: Product test


  Scenario: User can shop by category Face
   Given   User Open main page
    When   User Click on Shop by category
    Then   Verify face header is shown
    Then   Click on the face
    Then  Verify first product name face
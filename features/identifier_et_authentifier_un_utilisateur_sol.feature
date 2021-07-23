@JAMA-2711369 @JAMA-CM2-FEAT-25
Feature: Identifier et authentifier un utilisateur SOL
    [Jama](https://parkeon.jamacloud.com/perspective.req#/items/2711369?projectId=20386)

  @project-M2
  Scenario Outline: [US1.0] En tant qu'administrateur KeyCloak, je créé un utilisateur Sol afin qu'il puisse accéder au système CloudFare (<hiptest-uid>)
    "**Critères d'Acceptation**"
    - Un utilisateur avec des droits CloudFare est créé.
    Given G_open_session "KeyCloak" "administrateur" "" ""
    When W_open_module "m2a"
    And W_add_element "l'user" "<Username>"
    And W_insert_element "dans Credentials" "le mot de passe: <Password>"
    And W_assign_element "dans Role Mappings" "le role <Role>" "" ""
    Then T_create_element "Le nouvel user" "" "dans la liste d'usagers" ""

    Examples:
      | Realm | Username | Password | Role | hiptest-uid |
      | m2a | Tauto | Temporary | CloudFareWeb | uid:411e36cb-1ebd-46ee-8504-76db25b8c276 |

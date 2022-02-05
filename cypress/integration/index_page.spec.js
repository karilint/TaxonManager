// index_page.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe("TaxonManager", () => {
  beforeEach(function () {
    cy.visit("http://localhost:8000/");
  });
  it("Front page can be opened", () => {
    cy.contains("TaxonManager");
    cy.contains("Login");
    cy.contains("Features");
    cy.contains("Help");
    cy.contains("2022");
    cy.get("#mySidebar");

    //add reference button, not logged in
    cy.contains("Add reference").should("not.exist");
    cy.visit("http://localhost:8000/add_reference");
    cy.url().should("eq", "http://localhost:8000/");
  });
  it("Menu shows up on sidebar, on small screens", () => {
    //menu does not show on larger screens
    cy.get("#menuForSmallScreen").should("not.be.visible");

    // menu shows on small screen
    cy.viewport(990, 660);
    cy.get(".header-left .header-button").click();
    cy.contains("Menu");

    // menu's login button works
    cy.get("#menuForSmallScreen")
      .invoke("show")
      .contains("Login")
      .click({ force: true });
    cy.url().should("include", "login");

    // menu's help button works --will be updated when help page is established.
    cy.get(".header-left .header-button").click();
    cy.get("#menuForSmallScreen")
      .invoke("show")
      .contains("Help")
      .click({ force: true });
  });
  it("Front page adapts to logging in and logging out", () => {
    // front page contains login button but no logout button
    cy.get("#loginButton").should("exist");
    cy.get("#logout-button").should("not.exist");

    // login via the admin page to bypass orcid authentication
    cy.visit("http://localhost:8000/admin/login/?next=/admin/");
    cy.get("#id_username").type("testaaja");
    cy.get("#id_password").type("cypress");
    cy.contains("Log in").click();
    cy.visit("http://localhost:8000/");

    // front page contains logout button but no login button
    cy.get("#logoutButton").should("exist");
    cy.get("#login-button").should("not.exist");

    // logout through logout button
    cy.contains("Logout").click();

    // front page contains login button but no logout button
    cy.get("#loginButton").should("exist");
    cy.get("#logout-button").should("not.exist");
  });
});

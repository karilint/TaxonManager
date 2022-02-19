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
    cy.contains("Add reference")
    cy.get("#mySidebar");

  });
  it("Menu shows up on sidebar and adapts to logging in and out, on small screens", () => {
    //menu does not show on larger screens
    cy.get("#menuForSmallScreen").should("not.be.visible");

    // menu shows on small screen
    cy.viewport(990, 660);
    cy.get(".header-left .header-button").click();
    cy.contains("Menu");

    // menu contains login 
    cy.get("#menuForSmallScreen")
    cy.contains("Login")

    // login via the admin page to bypass orcid authentication
    cy.visit("http://localhost:8000/admin/login/?next=/admin/");
    cy.get("#id_username").type("testaaja");
    cy.get("#id_password").type("cypress");
    cy.contains("Log in").click();
    cy.visit("http://localhost:8000/");

    // menu contains logout button but no login button
    cy.get("#menuForSmallScreen")
    cy.contains("Logout").click({ force: true });

    // menu contains login button but no logout button
    cy.get("#menuForSmallScreen")
    cy.contains("Login")

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

  it("Create group and add user", () =>{
    cy.visit("http://localhost:8000/admin/login/?next=/admin/");
    cy.get("#id_username").type("testaaja");
    cy.get("#id_password").type("cypress");
    cy.contains("Log in").click();
    cy.visit("http://localhost:8000/admin/auth/group/add/");
    cy.get("#id_name").type("contributors2");
    cy.contains("Save and continue").click();

    //add testaaja to the group
    cy.contains("Users").click();
    cy.get('#main').contains('testaaja').click();
    cy.contains("Choose all").click();
    cy.contains("Save and continue").click();
  });

  it("Adding references works", () => {
    // front page contains login button but no logout button
    cy.get("#loginButton").should("exist");
    cy.get("#logout-button").should("not.exist");

    // login via the admin page to bypass orcid authentication
    cy.visit("http://localhost:8000/admin/login/?next=/admin/");
    cy.get("#id_username").type("testaaja");
    cy.get("#id_password").type("cypress");
    cy.contains("Log in").click();

    cy.visit("http://localhost:8000/add-references/");

    // Add references page contains Add or Edit Reference
    cy.contains("Add or Edit Reference");

    // Add references page contains form for adding or editing
    // cy.get("#add-ref-form").should("exist");

    // Insert reference details
    cy.get("#id_authors").type("Testi Kirjoittaja");
    cy.get("#id_title").type("Testi otsikko");
    cy.get("#id_year").type("2022");

    // Submit
    cy.contains("Submit").click();

    // Visit
    cy.visit("http://localhost:8000/references/");

    // Check if reference can be found on page
    cy.contains("Testi Kirjoittaja");
    cy.contains("Logout").click({ force: true });
  });
  it("Logged in user that not part of group contributors", () => {
    // login via the admin page to bypass orcid authentication
    cy.visit("http://localhost:8000/admin/login/?next=/admin/");
    cy.get("#id_username").type("testaaja");
    cy.get("#id_password").type("cypress");
    cy.contains("Log in").click();

    //remove user from group
    cy.contains("Users").click();
    cy.get('#main').contains('testaaja').click();
    cy.contains("Remove all").click();
    cy.contains("Save and continue").click();
    
    //check view when user not part of group
    cy.visit("http://localhost:8000/add-references/");
    cy.contains("Add or Edit Reference").should("not.exist");
  });
});


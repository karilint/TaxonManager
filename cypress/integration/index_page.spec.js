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
    cy.contains("Add reference");
    cy.contains("Welcome");
    cy.get("#mySidebar");

    cy.contains("TaxonManger is a tool for classifying fossil species.");
    cy.contains("In the scientific classification of fossil species, organisms are organized into hierarchical categories, taxa. Different taxon levels include, for example, class, order, tribe, genus, and species. As research progresses, knowledge about the relationships of the species also increases, which may lead to changes in their taxonomy.");
    cy.contains("2022 - TaxonManager");

    // images shown with credits on frontpage
    cy.get(".image_text").should("exist");
    cy.contains("Picture © Luonnontieteellinen Keskusmuseo");
    cy.get("#header_image");
    cy.contains("Picture_©_Noira_Martiskainen");

  });
  it("Menu shows up on sidebar and adapts to logging in and out, on small screens", () => {
    //menu does not show on larger screens
    cy.get("#menuForSmallScreen").should("not.be.visible");

    // menu shows on small screen
    cy.viewport(990, 660);
    cy.get("Welcome").should("not.exist");
    cy.get(".header-left .header-button").click();
    cy.contains("Menu");

    // images shown on small screen
    cy.get(".image_text").should("exist");
    cy.contains("Picture © Luonnontieteellinen Keskusmuseo");
    cy.get("#header_image");
    cy.contains("Picture_©_Noira_Martiskainen");
    
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
    // front page contains information about login in
    cy.contains("Hello guest! Log in with your ORCID account. Upon the first time of use we will send an e-mail to you for verification. Please follow the link provided to finalize the signup process.");

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

    // front page shows username
    cy.contains("Hello, testaaja! You are logged in.");

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

    // Add references page contains Add or Edit Reference and other tags
    cy.contains("Add or Edit Reference");
    cy.contains("Reference List");
    cy.contains("Add a reference");
    cy.contains("Search");
    // Add references page contains form for adding or editing
    // cy.get("#add-ref-form").should("exist");

    // Insert reference details
    cy.get("#id_authors").type("Testi Kirjoittaja");
    cy.get("#id_title").type("Testi otsikko");
    cy.get("#id_year").type("2022");

    // Submit
    cy.contains("Submit").click();

    // Add reference using DOI
    cy.visit("http://localhost:8000/add-references/");
    cy.get("#id_doi").type("10.1109/SMC.2016.7844781");
    cy.contains("Submit").click();

    // check that added references are listed
    cy.visit("http://localhost:8000/references/");
    cy.contains("Testi Kirjoittaja");
    cy.contains("10.1109/SMC.2016.7844781");

    cy.contains("Logout").click({ force: true });
  });
  it("Edit and delete reference", () => {
    // login via the admin page to bypass orcid authentication
    cy.visit("http://localhost:8000/admin/login/?next=/admin/");
    cy.get("#id_username").type("testaaja");
    cy.get("#id_password").type("cypress");
    cy.contains("Log in").click();

    cy.visit("http://localhost:8000/add-references/1");

    // Edit reference
    cy.get("#id_title").clear();
    cy.get("#id_title").type("Another Title");
    cy.contains("Submit").click();
    cy.visit("http://localhost:8000/references/");

    // Check if reference has been updated
    cy.contains("Another Title");

    // revert back
    cy.visit("http://localhost:8000/add-references/1");
    cy.get("#id_title").clear();
    cy.get("#id_title").type("Testi otsikko");
    cy.contains("Submit").click();

    //Delete reference

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

  it("Search references", () => { 
    cy.contains("References").click();
    cy.contains("Search").click();

    // Search reference with no input
    cy.get(".btn").click();
    cy.contains("2 Results");

    // Search reference with correct input
    cy.get("#id_title").type("Testi otsikko");
    cy.get(".btn").click();
    cy.contains("1 Results");

    // Search reference with wrong input
    cy.get("#id_title").type("0");
    cy.get(".btn").click();
    cy.contains("0 Results");

    // Search reference with DOI
    //cy.get("#id_title").clear();
    //cy.get("#id_doi").type("10.1109/SMC.2016.7844781");
    //cy.get(".btn").click();
    //cy.contains("1 Results");
    
  });

  it("Adding Authors", () => {
    cy.visit("http://localhost:8000/admin/login/?next=/admin/");
    cy.get("#id_username").type("testaaja");
    cy.get("#id_password").type("cypress");
    cy.contains("Log in").click();

    cy.visit("http://localhost:8000/add-author/");
    cy.contains("Add author")

  })

  it("Viewing Authors", () => {
    cy.visit("http://localhost:8000/admin/login/?next=/admin/");
    cy.get("#id_username").type("testaaja");
    cy.get("#id_password").type("cypress");
    cy.contains("Log in").click();

    cy.visit("http://localhost:8000/authors/");
    cy.contains("Authors")
  
  })

  it("Viewing Taxa", () => {
    cy.visit("http://localhost:8000/admin/login/?next=/admin/");
    cy.get("#id_username").type("testaaja");
    cy.get("#id_password").type("cypress");
    cy.contains("Log in").click();

    cy.visit("http://localhost:8000/taxa/");
    cy.contains("Animalia")
    cy.contains("Bacteria")
  
  })
});
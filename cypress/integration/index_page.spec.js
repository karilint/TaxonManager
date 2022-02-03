// index_page.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe("TaxonManager", () => {
  beforeEach(function() {
    cy.visit("http://localhost:8000/")
  })
  it("Front page can be opened", () => {
    cy.contains("TaxonManager")
    cy.contains("Login")
    cy.contains("Features")
    cy.contains("Help")
    cy.contains("2022")
    cy.get('#mySidebar')
  })
  it("Menu shows up on sidebar, on small screens", () => {
    //menu does not show on larger screens
    cy.get("#menuForSmallScreen").should('not.be.visible')

    // menu shows on small screen
    cy.viewport(990, 660);
    cy.get(".header-left .header-button").click()
    cy.contains("Menu")
    
    // menu's login button works
    cy.get("#menuForSmallScreen").invoke('show').contains("Login").click({force:true})
    cy.url().should("include", "login")

    // menu's help button works --will be updated when help page is established.
    cy.get(".header-left .header-button").click()
    cy.get("#menuForSmallScreen").invoke('show').contains("Help").click({force:true})       
  })
})

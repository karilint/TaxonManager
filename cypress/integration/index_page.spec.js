// index_page.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('TaxonManager', () => {
    it('Front page can be opened', () => {
      cy.visit('http://localhost:8000/')
      cy.contains('TaxonManager')
    })
  })
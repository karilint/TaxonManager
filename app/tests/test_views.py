from django.test import TestCase
from django.contrib.auth.models import User


class StatuscodeTest(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(username='Elon Musk')

    def test_index_page_returns_ok(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_references_page_returns_ok(self):
        response = self.client.get('/references/')
        self.assertEqual(response.status_code, 200)

    def test_taxa_page_returns_ok(self):
        response = self.client.get('/taxa/')
        self.assertEqual(response.status_code, 200)

    def test_authors_page_returns_ok(self):
        response = self.client.get('/authors/')
        self.assertEqual(response.status_code, 200)

    def test_experts_page_returns_ok(self):
        response = self.client.get('/experts/')
        self.assertEqual(response.status_code, 200)
    
    def test_taxa_search_page_returns_ok(self):
        response = self.client.get('/taxa-search/')
        self.assertEqual(response.status_code, 200)

    def test_add_reference_page_returns_ok_after_logging_in(self):
        self.client.force_login(self.test_user)
        response = self.client.get('/add-references/')
        self.assertEqual(response.status_code, 200)

    def test_addname_page_returns_ok_after_logging_in(self):
        self.client.force_login(self.test_user)
        response = self.client.get('/add-taxon/')
        self.assertEqual(response.status_code, 200)

    def test_add_author_page_returns_ok_after_logging_in(self):
        self.client.force_login(self.test_user)
        response = self.client.get('/add-author/')
        self.assertEqual(response.status_code, 200)

    def test_add_expert_page_returns_ok_after_logging_in(self):
        self.client.force_login(self.test_user)
        response = self.client.get('/add-expert/')
        self.assertEqual(response.status_code, 200)


class TemplateTest(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(username='Elon Musk')

    def test_index_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'front/index.html')

    def test_references_page_uses_correct_template(self):
        response = self.client.get('/references/')
        self.assertTemplateUsed(response, 'front/references.html')

    def test_taxa_page_uses_correct_template(self):
        response = self.client.get('/taxa/')
        self.assertTemplateUsed(response, 'front/taxa.html')

    def test_authors_page_uses_correct_template(self):
        response = self.client.get('/authors/')
        self.assertTemplateUsed(response, 'front/authors.html')

    def test_experts_page_uses_correct_template(self):
        response = self.client.get('/experts/')
        self.assertTemplateUsed(response, 'front/experts.html')

    def test_taxa_search_page_uses_correct_template(self):
        response = self.client.get('/taxa-search/')
        self.assertTemplateUsed(response, 'front/taxa-search.html')

    def test_add_reference_page_uses_correct_template(self):
        self.client.force_login(self.test_user)
        response = self.client.get('/add-references/')
        self.assertTemplateUsed(response, 'front/add-reference.html')

    def test_addname_page_uses_correct_template(self):
        self.client.force_login(self.test_user)
        response = self.client.get('/add-taxon/')
        self.assertTemplateUsed(response, 'front/add-taxon.html')

    def test_add_author_page_uses_correct_template(self):
        self.client.force_login(self.test_user)
        response = self.client.get('/add-author/')
        self.assertTemplateUsed(response, 'front/add-author.html')

    def test_add_expert_page_uses_correct_template(self):
        self.client.force_login(self.test_user)
        response = self.client.get('/add-expert/')
        self.assertTemplateUsed(response, 'front/add-expert.html')



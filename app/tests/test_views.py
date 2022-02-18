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

    def test_add_reference_page_returns_redirect_before_logging_in(self):
        response = self.client.get('/add-references/')
        self.assertEqual(response.status_code, 302)

    def test_add_reference_page_returns_ok_after_logging_in(self):
        self.client.force_login(self.test_user)
        response = self.client.get('/add-references/')
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

    def test_add_reference_page_uses_correct_template(self):
        self.client.force_login(self.test_user)
        response = self.client.get('/add-references/')
        self.assertTemplateUsed(response, 'front/add_reference.html')


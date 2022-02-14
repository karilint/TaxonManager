from django.test import TestCase

class StatuscodeTest(TestCase):
    def test_index_page_responses_ok(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_references_page_responses_ok(self):
        response = self.client.get('/references/')
        self.assertEqual(response.status_code, 200)

    def test_add_reference_page_responses_redirect(self):
        response = self.client.get('/add_reference')
        self.assertEqual(response.status_code, 301)

class TemplateTest(TestCase):
    def test_index_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'front/index.html')
    def test_references_page_uses_correct_template(self):
        response = self.client.get('/references/')
        self.assertTemplateUsed(response, 'front/references.html')

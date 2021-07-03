from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string


from .views import home_page

class HomePageTest(TestCase):
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

    # def test_home_page_returns_correct_html(self):
    #     '''тест: домашняя страница возвращает правильный html'''
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('utf8')
    #     # self.assertTrue(html.startswith('<html>'))
    #     # self.assertIn('<title>To-Do lists</title>', html)
    #     # self.assertTrue(html.endswith('</html>'))
    #     # self.assertTrue(html.strip().endswith('</html>'))
    #     expected_html = render_to_string('home.html')
    #     self.assertEqual(html, expected_html)

    # def test_home_page_returns_correct_html(self):
    #     response = self.client.get('/')
    #
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))
    #
    #     self.assertTemplateUsed(response, 'home.html')

    # def test_uses_home_template(self):
    #     '''тест домашней страницы'''
    #     '''тест: используется домашний шаблон'''
    #     response = self.client.get('/')
    #     self.assertTemplateUsed(response, 'home.html')

    def test_uses_home_template(self):
        '''тест: используется домашний шаблон'''

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        '''тест: можно сохранить post-запрос'''
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


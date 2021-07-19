from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException
import unittest

MAX_WAIT = 10

# browser = webdriver.Firefox()
# browser.get('http://localhost:8222')
# assert 'Django' in browser.title
# # assert 'To-Do' in browser.title
# browser.quit()

class NewVisitorTest(LiveServerTestCase):
    '''тест нового посетителя'''

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()






    def wait_for_row_in_list_table(self, row_text):
        '''ожидать строку в таблице списка'''

        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    # def test_can_start_a_list_and_retrieve_it_later(self):
        # self.browser.get(self.live_server_url)
        # # self.browser.get('http://localhost:8222')
        # self.assertIn('To-Do', self.browser.title)
        # header_text = self.browser.find_element_by_tag_name('h1').text
        # # print(777, self.browser.title)
        # self.assertIn('To-Do', header_text)
        #
        # inputbox = self.browser.find_element_by_id('id_new_item')
        # self.assertEqual(
        #     inputbox.get_attribute('placeholder'),
        #     'Enter a to-do item'
        # )
        # inputbox.send_keys('Купить павлиньи перья')
        # inputbox.send_keys(Keys.ENTER)
        # # time.sleep(3)
        # self.wait_for_row_in_list_table('1: Купить павлиньи перья')
        #
        # inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys('Сделать мушку из павлиньих перьев')
        # inputbox.send_keys(Keys.ENTER)
        # # time.sleep(1)
        #
        # # Страница снова обновляется и теперь показывает оба элемента ее списка
        # self.wait_for_row_in_list_table('1: Купить павлиньи перья')
        # self.wait_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')
        #
        #
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # # self.assertTrue(
        # #     any(row.text == '1: Купить павлиньи перья' for row in rows)
        # # )
        # # self.assertTrue(
        # #     any(row.text == '1: Купить павлиньи перья' for row in rows),
        # #     f"Новый элемент списка не появился в таблице. Содержимым было:"
        # #     f"\n{table.text}"
        # # )
        # self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])
        # self.assertIn(
        #     '2: Сделать мушку из павлиньих перьев',
        #     [row.text for row in rows]
        # )
        # # Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
        # # сайт сгенерировал для нее уникальный URL-адрес – по этому поводу
        # # выводится небольшой текст с объяснениями.
        #
        # self.fail('Закончить тест!')
        #
        # # Она посещает этот URL-адрес – ее список по-прежнему там.
        # # Удовлетворенная, она снова ложится спать.

    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)
        # self.browser.get('http://localhost:8222')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        # print(777, self.browser.title)
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(3)
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)

        # Страница снова обновляется и теперь показывает оба элемента ее списка
        self.wait_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')
        # Удовлетворенная, она снова ложится спать.

    def test_multiple_users_can_start_lists_at_different_urls(self):
        '''тест: многочисленные пользователи могут начать списки по разным url'''
        # Эдит начинает новый список
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')

        # Она замечает, что ее список имеет уникальный URL-адрес
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        # Теперь новый пользователь, Фрэнсис, приходит на сайт.

        ## Мы используем новый сеанс браузера, тем самым обеспечивая, чтобы никакая
        ## информация от Эдит не прошла через данные cookie и пр.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Фрэнсис посещает домашнюю страницу. Нет никаких признаков списка Эдит
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Купить павлиньи перья', page_text)
        self.assertNotIn('Сделать мушку', page_text)

        # Фрэнсис начинает новый список, вводя новый элемент. Он менее
        # интересен, чем список Эдит...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Купить молоко')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Купить молоко')

        # Фрэнсис получает уникальный URL-адрес
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Опять-таки, нет ни следа от списка Эдит
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Купить павлиньи перья', page_text)
        self.assertIn('Купить молоко', page_text)

        # Удовлетворенные, они оба ложатся спать

# if __name__ == '__main__':
#     unittest.main(warnings='ignore')

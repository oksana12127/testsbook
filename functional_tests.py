from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest



# browser = webdriver.Firefox()
# browser.get('http://localhost:8222')
# assert 'Django' in browser.title
# # assert 'To-Do' in browser.title
# browser.quit()

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        '''подтверждение строки в таблице списка'''

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8222')
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
        time.sleep(3)
        self.check_for_row_in_list_table('1: Купить павлиньи перья')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        # Страница снова обновляется и теперь показывает оба элемента ее списка
        self.check_for_row_in_list_table('1: Купить павлиньи перья')
        self.check_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')


        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1: Купить павлиньи перья' for row in rows)
        # )
        # self.assertTrue(
        #     any(row.text == '1: Купить павлиньи перья' for row in rows),
        #     f"Новый элемент списка не появился в таблице. Содержимым было:"
        #     f"\n{table.text}"
        # )
        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])
        self.assertIn(
            '2: Сделать мушку из павлиньих перьев',
            [row.text for row in rows]
        )
        self.fail('Закончить тест!')





if __name__ == '__main__':
    unittest.main(warnings='ignore')

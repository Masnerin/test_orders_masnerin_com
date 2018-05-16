# Тестирование формы заказа.
# Студия Маснерин (http://www.masnerin.com)

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class MasnerinOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Masnerin\\WebDriver\\Chrome\\chromedriver.exe')

    def test_orders_in_masnerin_com(self):
        driver = self.driver
        driver.get("http://www.masnerin.com/index.php/orders")
        self.driver.maximize_window()
        self.assertIn("Заказать", driver.title)

        elem = driver.find_element_by_name("text0105")
        elem.send_keys("Сергей")

        elem = driver.find_element_by_name("email1105")
        elem.send_keys("davydovsa@hotmail.com")

        select = Select(driver.find_element_by_name('select2105'))
        select.select_by_value('Оцифровка') 

        elem = driver.find_element_by_name("textarea3105")
        elem.send_keys("Проводится тестирование формы заказа на сайте www.masnerin.com")

        button = driver.find_element_by_id("submit105")
        button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    

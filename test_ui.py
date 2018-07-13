import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PythonOrgTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_python_org(self):
        self.driver.get('https://www.python.org')
        time.sleep(5)
        # self.assertIn('Python', self.driver.title)
        self.driver.find_element_by_link_text("Downloads").click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'wadget-title'))
        )
        self.assertEqual('Looking for a specific release?', element.text)





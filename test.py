#! python3
from selenium import webdriver
import unittest

class New(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
    def tearDown(self):
        self.driver.quit()
    def test_later(self):
        self.driver.get('http://localhost:8000')
        self.fail('Finish the test!')

if __name__=='__main__':
    unittest.main(warnings='ignore')


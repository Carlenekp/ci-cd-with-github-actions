import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TestAppE2E(unittest.TestCase):
    def setUp(self):
        # Launch your flask app first
        #self.driver = webdriver.Chrome("C:/Users/carle/OneDrive/Bureau/chrome-win64")
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000')

    def test_add_and_delete_item(self):
        # you can use the driver to find elements in the page
        # example:
        
        # this refers to the 'name="item"' attribute of the html element
        # checkout the rest of the methods in the documentation:
        # https://selenium-python.readthedocs.io/locating-elements.html
        
        # after you select your element, you can send it a key press:
       
        
        # and you can use the rest of the assetion methods as well:
       
        item = self.driver.find_element(By.NAME, 'item')
        item.send_keys('New E2E Item')
        item.send_keys(Keys.RETURN)
        #check if it is there
        self.assertIn('New E2E Item', self.driver.page_source)

        delete = self.driver.find_element(By.XPATH, "/html/body/div/ul/li/a")
        delete.click()
        #check if it is not there
        self.assertNotIn('New E2E Item', self.driver.page_source)


        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

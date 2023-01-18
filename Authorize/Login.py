import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from data import alldata

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_Login_Positif(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"input#email").send_keys(alldata.email) # isi email
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys(alldata.password) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#signin_login").click()
        time.sleep(3)

        response_message = driver.find_element(By.CSS_SELECTOR,"h2#swal2-title").text
        self.assertEqual(response_message, 'Welcome Renal')

    def test_Login_Negatif_BlankPassword(self): 
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"input#email").send_keys(alldata.email) # isi email
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # blank password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#signin_login").click()
        time.sleep(3)

        response_message = driver.find_element(By.CSS_SELECTOR,"h2#swal2-title").text
        self.assertEqual(response_message, "User's not found")

unittest.main()
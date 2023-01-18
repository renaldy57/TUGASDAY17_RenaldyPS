import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from data import alldata

class TestSignUp(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_SignUp_Positif(self): #Ubah email atau passwordnya jika ingin run ini success
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"button#signUp").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#name_register").send_keys(alldata.name) # isi name
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#email_register").send_keys(alldata.email) # isi email
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password_register").send_keys(alldata.password) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#signup_register").click()
        time.sleep(3)

        response_message = driver.find_element(By.CSS_SELECTOR,"h2#swal2-title").text
        self.assertEqual(response_message, 'berhasil')

    def test_SignUp_Negatif_BlankEmail(self): 
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"button#signUp").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#name_register").send_keys(alldata.name) # isi name
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#email_register").send_keys("") # blank email
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password_register").send_keys(alldata.password) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#signup_register").click()
        time.sleep(3)

        response_message = driver.find_element(By.CSS_SELECTOR,"div#swal2-content").text
        self.assertEqual(response_message, 'Gagal Register!')

    def test_SignUp_Negatif_UserAlreadyExist(self): 
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"button#signUp").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#name_register").send_keys(alldata.name) # isi name
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#email_register").send_keys(alldata.email) # isi email
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password_register").send_keys(alldata.password) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#signup_register").click()
        time.sleep(3)

        response_message = driver.find_element(By.CSS_SELECTOR,"div#swal2-content").text
        self.assertEqual(response_message, 'Gagal Register!')

unittest.main()
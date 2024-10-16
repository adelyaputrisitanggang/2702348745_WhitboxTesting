from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import unittest

class AssessmentViewTest(unittest.TestCase):
    def setUp(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("window-size=1920,1080")

        service = Service('/usr/local/bin/chromedriver-mac-arm64/chromedriver')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def test_assessment_page(self):
        driver = self.driver

        driver.get('https://newbinusmaya.binus.ac.id/lms/dashboard')
        driver.maximize_window()

        try:
            print("Waiting for the username input field...")
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "username")))
            username = driver.find_element(By.ID, "username")
            print("Username element found!")
        except Exception as e:
            print(f"Error finding username field: {e}")
            print(driver.page_source)
            return

        assert username.is_displayed(), "Username field is not visible"
        assert username.is_enabled(), "Username field is not enabled"

        print("Trying to enter the email...")
        username.clear()
        username.send_keys("adelya.sitanggang@binus.ac.id")

        # Fallback using JavaScript if send_keys doesn't work
        driver.execute_script("arguments[0].value = 'adelya.sitanggang@binus.ac.id';", username)

        print("Waiting for the password input field...")
        password = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password.click()
        password.send_keys("kuubah")

        password.send_keys(Keys.RETURN)

        print("Waiting for dashboard to load...")
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.CLASS_NAME, "actual-dashboard-class"))
        )


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

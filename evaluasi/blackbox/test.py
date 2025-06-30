from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://organic-goldfish-wr4v7v79q9xqc66v-5000.app.github.dev/"  # Ganti dengan URL publik Codespaces

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Gunakan Service() sesuai versi Selenium 4
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get(URL)
    time.sleep(1)

    upload = driver.find_element(By.NAME, "file")
    upload.send_keys("/workspaces/ML_Plant_Clasification_Using_Leaf/test_leaf.jpg")

    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
    time.sleep(3)

    assert "Hasil Deteksi" in driver.page_source or "Detected" in driver.page_source
    print("✅ TEST PASSED")

except Exception as e:
    print("❌ TEST FAILED:", e)

finally:
    driver.quit()

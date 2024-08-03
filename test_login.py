import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Konfigurasi ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Jika ingin menjalankan browser tanpa tampilan GUI
chrome_service = Service('C:\\chromedriver-win64\\chromedriver.exe')  # Sesuaikan path dengan lokasi chromedriver Anda

# Inisialisasi WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

try:
    logging.info("Opening saucedemo.com")
    driver.get("https://www.saucedemo.com/")

    logging.info("Waiting for username and password fields")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )

    # Temukan elemen input username dan password
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")

    # Masukkan username dan password
    logging.info("Entering username and password")
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")

    # Klik tombol login
    logging.info("Clicking login button")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Tambah waktu tunggu untuk halaman berikutnya
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Verifikasi login berhasil
    logging.info("Verifying login success")
    assert "Products" in driver.page_source, "Login failed or redirected to wrong page"
    logging.info("Login successful and test passed!")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    # Ambil screenshot untuk debugging
    driver.save_screenshot('after_login.png')
    logging.info("Screenshot saved as after_login.png")

    # Tutup browser
    driver.quit()
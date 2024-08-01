from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Konfigurasi ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Jika ingin menjalankan browser tanpa tampilan GUI
chrome_service = Service('C:\\chromedriver-win64\\chromedriver.exe')  # Sesuaikan path dengan lokasi chromedriver Anda

# Inisialisasi WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

try:
    # Buka halaman login
    driver.get("https://www.saucedemo.com/")
    print("Opened saucedemo.com")

    # Tunggu hingga elemen username dan password muncul
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    print("Username and password fields are present")

    # Temukan elemen input username dan password
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")

    # Masukkan username dan password
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")

    # Klik tombol login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    print("Clicked login button")

    # Tambah waktu tunggu untuk halaman berikutnya
    time.sleep(5)

    # Ambil screenshot untuk debugging
    driver.save_screenshot('after_login.png')

    # Cetak HTML halaman setelah login
    page_source = driver.page_source
    with open("after_login.html", "w", encoding="utf-8") as f:
        f.write(page_source)

    # Tunggu hingga elemen dengan teks "Products" muncul menggunakan XPath
    title_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Products']"))
    )
    print("Title element is present")

    # Verifikasi login berhasil
    title = title_element.text
    assert title == "Products", "Login failed or redirected to wrong page"
    print("Login successful and test passed!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Tutup browser
    driver.quit()
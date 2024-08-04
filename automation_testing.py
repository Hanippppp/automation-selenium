from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
import time

driver = webdriver.Chrome()

def login():
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    print("Login successful")

def validate_login():
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item')))
        return True
    except TimeoutException:
        return False

def retry_find_element(driver, by, value, retries=3, delay=1):
    """ Retry finding an element to handle StaleElementReferenceException """
    for _ in range(retries):
        try:
            element = driver.find_element(by, value)
            return element
        except StaleElementReferenceException:
            time.sleep(delay)
    raise StaleElementReferenceException("Element could not be found after several retries")

def retry_click(driver, by, value, retries=3, delay=1):
    """ Retry finding and clicking an element to handle StaleElementReferenceException """
    for _ in range(retries):
        try:
            element = driver.find_element(by, value)
            element.click()
            return
        except StaleElementReferenceException:
            time.sleep(delay)
    raise StaleElementReferenceException("Element could not be clicked after several retries")

def test_add_to_cart_and_remove():
    wait = WebDriverWait(driver, 10)
    
    # Add to cart
    add_to_cart_button = retry_find_element(driver, By.XPATH, "//button[text()='Add to cart']")
    add_to_cart_button.click()
    time.sleep(1)  # Jeda 1 detik setelah Add to Cart
    
    # Verify item added to cart
    cart_count = retry_find_element(driver, By.CLASS_NAME, 'shopping_cart_badge').text
    assert cart_count == '1', f"Expected cart count to be 1 but got {cart_count}"
    print("Add to cart functionality tested")
    
    # Remove from cart
    remove_button = retry_find_element(driver, By.XPATH, "//button[text()='Remove']")
    remove_button.click()
    time.sleep(1)  # Jeda 1 detik setelah Remove
    
    # Verify item removed from cart
    try:
        cart_count = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    except NoSuchElementException:
        cart_count = ''
    assert cart_count == '', f"Expected cart count to be empty but got {cart_count}"
    print("Remove from cart functionality tested")

def test_product_detail_add_remove():
    # Klik salah satu produk
    product_link = retry_find_element(driver, By.CLASS_NAME, 'inventory_item_name')
    product_link.click()
    time.sleep(1)  # Jeda 1 detik setelah mengklik produk

    # Periksa apakah produk sudah ada di keranjang
    try:
        remove_button = driver.find_element(By.XPATH, "//button[text()='Remove']")
        is_in_cart = True
    except NoSuchElementException:
        is_in_cart = False

    if is_in_cart:
        # Jika produk sudah ada di keranjang, klik remove
        remove_button.click()
        time.sleep(1)  # Jeda 1 detik setelah remove
        print("Product removed from cart")
    else:
        # Jika produk belum ada di keranjang, klik add to cart
        add_to_cart_button = retry_find_element(driver, By.XPATH, "//button[text()='Add to cart']")
        add_to_cart_button.click()
        time.sleep(1)  # Jeda 1 detik setelah add to cart
        print("Product added to cart")

    # Kembali ke halaman inventory
    back_to_products_button = retry_find_element(driver, By.ID, 'back-to-products')
    back_to_products_button.click()
    print("Back to products page")

def add_all_products_to_cart():
    # Menambahkan semua produk ke keranjang
    inventory_items = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    print(f"Total inventory items: {len(inventory_items)}")
    
    for item in inventory_items:
        try:
            add_button = item.find_element(By.XPATH, ".//button[text()='Add to cart']")
            add_button.click()
            time.sleep(1)  # Jeda 1 detik setelah menambahkan setiap produk ke keranjang
        except NoSuchElementException:
            print(f"Item already in cart, skipping to next item: {item.find_element(By.CLASS_NAME, 'inventory_item_name').text}")
    print("All products added to cart")

def verify_cart_contents():
    # Klik ikon keranjang
    cart_icon = retry_find_element(driver, By.CLASS_NAME, 'shopping_cart_link')
    cart_icon.click()
    time.sleep(1)  # Jeda 1 detik setelah mengklik ikon keranjang

    # Verifikasi bahwa semua produk ada di keranjang
    cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')
    print(f"Total items in cart: {len(cart_items)}")
    inventory_items = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    print(f"Expected items in cart: {len(inventory_items)}")
    
    assert len(cart_items) == len(inventory_items), "Not all items were added to the cart"
    print("All items verified in cart")

def main():
    login()
    time.sleep(1)  # Jeda 1 detik setelah login
    if validate_login():
        time.sleep(1)  # Jeda 1 detik setelah validasi login
        test_add_to_cart_and_remove()
        time.sleep(1)  # Jeda 1 detik setelah pengujian Add to Cart dan Remove
        test_product_detail_add_remove()
        time.sleep(1)  # Jeda 1 detik setelah pengujian detail produk
        add_all_products_to_cart()
        time.sleep(1)  # Jeda 1 detik setelah menambahkan semua produk ke keranjang
        verify_cart_contents()
    driver.quit()

if __name__ == "__main__":
    main()
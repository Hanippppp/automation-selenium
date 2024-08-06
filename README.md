# Saucedemo Automation Testing

This project aims to automate the testing process on the Saucedemo website using Python, Selenium, and Chromedriver.

## Project Structure

This project consists of the following files:

- `saucedemo_test.py`: The main script used to run the Selenium tests.
- `requirements.txt`: A file containing the list of libraries required to run this project.

## How to Run the Tests

Follow these steps to run the tests:

1. **Clone this repository**:
    ```bash
    git clone https://github.com/yourusername/saucedemo-automation-testing.git
    cd saucedemo-automation-testing
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate  # For Windows
    ```

3. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Selenium tests**:
    ```bash
    python saucedemo_test.py
    ```

The script will perform the following actions:
- Log in to the Saucedemo website.
- Navigate to a product's detail page, add the product to the cart, and remove it.
- Add all products to the cart from the inventory page.
- Verify the items in the cart.
- Remove an item from the cart.
- Proceed to checkout, fill in the checkout information, and complete the order.

## Dataset Explanation

- `saucedemo_test.py`: Contains the script for automating the tests on the Saucedemo website, including login, cart operations, and checkout process.
- `requirements.txt`: Lists all the Python dependencies required for this project.

## Visualizations and Analysis

The tests include various operations such as:
- Logging in to the website.
- Adding and removing products from the cart.
- Proceeding through the checkout process and completing the order.

## Contact

If you have any questions or suggestions, feel free to contact me at [email@example.com](mailto:email@example.com).

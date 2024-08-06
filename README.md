# Saucedemo Automation Testing

This project demonstrates how to use Python, Selenium, and Chromedriver for automating the testing process on the [Saucedemo](https://www.saucedemo.com/) website. The tests include logging in, adding and removing items from the cart, and completing the checkout process.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Tests Included](#tests-included)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/saucedemo-automation-testing.git
   cd saucedemo-automation-testing
Create a virtual environment and activate it:

sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

sh
Copy code
pip install -r requirements.txt
Download Chromedriver:
Ensure you have Chromedriver installed and it's compatible with your Chrome browser version. You can download it from here.

Add Chromedriver to your PATH:

On macOS/Linux:
sh
Copy code
export PATH=$PATH:/path/to/chromedriver
On Windows:
Add the Chromedriver directory to the system PATH.
Usage
Run the test script:

sh
Copy code
python saucedemo_test.py
The script will:

Log in to the Saucedemo website.
Add and remove items from the cart.
Proceed through the checkout process and complete the order.
Project Structure
plaintext
Copy code
saucedemo-automation-testing/
│
├── saucedemo_test.py     # Main script containing the Selenium tests
├── requirements.txt      # List of Python dependencies
└── README.md             # Project README file
Tests Included
Login:

Navigates to the login page and logs in using valid credentials.
Product Details and Cart Operations:

Navigates to a product's detail page, adds the product to the cart, and removes it.
Adds all products to the cart from the inventory page.
Cart Verification and Checkout:

Verifies the items in the cart.
Removes an item from the cart.
Proceeds to checkout and fills in the checkout information.
Completes the order by clicking the Finish button.
Contributing
Contributions are welcome! Please submit a pull request or open an issue for any improvements or additions.

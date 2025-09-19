# 🧪 Selenium UI Automation Framework  
**PyTest-and-Selenium Demo — Finexus Home Assessment**  
This is a demo project to showcase my skills in Python UI test automation using the **PyTest** and **Selenium** frameworks.

---

## 📁 Project Structure

```
.
├── config/
│   └── config.ini              # Configuration file for credentials and URLs
├── pages/
│   ├── login_page.py           # LoginPage class (Page Object)
│   └── secure_area_page.py     # SecureAreaPage class (Page Object)
├── tests/
│   └── test_login.py           # Login test case using Page Objects
├── html_reports/               # Auto-generated PyTest HTML reports
├── main.py                     # Script to run tests and generate reports
├── conftest.py                 # Pytest fixtures (e.g., WebDriver setup/teardown)
├── requirements.txt
└── README.md                   
```

---

## 🚀 Getting Started

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/wan-iqra/Home_Assessment.git
cd path-to-repo
```

---

### ✅ 2. Set Up the Environment

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

### ✅ 3. Configure Credentials and URLs

Edit the `config/config.ini` file (below are examples only, actual configuration is different):

```ini
[credentials]
email = your_email@example.com
password = your_password

[urls]
login_page = https://your-app.com/login
```

---

## 🧪 Running Tests

### 🔹 Option 1: Run main.py via HTML-PyTest 

Reminder: make sure the lines 10-25 in main.py are uncommented, while others commented

<img width="656" height="410" alt="image" src="https://github.com/user-attachments/assets/1272e339-35e0-400f-972a-506e07e2a94a" />

This will:

- Run all test cases  
- Generate an HTML report in `reports_html/`  
- Automatically open the report in your default web browser

HTML Report Example:

<img width="652" height="544" alt="image" src="https://github.com/user-attachments/assets/0e5c4d73-e2f8-4bab-ba32-4b1469c5c1e3" />

---

### 🔹 Option 2: Run with Allure Reporting (if configured)

Reminder: make sure the lines 29-36 in main.py are uncommented, while others commented

<img width="575" height="225" alt="image" src="https://github.com/user-attachments/assets/2352a3c4-59d2-466b-a287-f1254a27f7ae" />

This will:

- Run all test cases  
- Generate an interactive Allure report in `reports_allure/`  
- Automatically open the report in your default web browser

> ✅ **Note:** Ensure Allure CLI is installed. [Install Allure CLI](https://docs.qameta.io/allure/#_installing_a_commandline)

If Allure CLI is not installed, try run these 2 commands in Powershell in scoop:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```
Then install allure:
```bash
scoop install allure
```
Check version of installed allure using allure --version:

<img width="615" height="183" alt="image" src="https://github.com/user-attachments/assets/2ffeabec-3784-49e3-aac7-af8c894a50d4" />

Allure Report Example:

<img width="864" height="769" alt="image" src="https://github.com/user-attachments/assets/fc3f4db3-da53-4f26-b710-871a1201d0e6" />

---

## 🧰 Tools & Dependencies

- Python 3.8+
- Selenium
- PyTest
- pytest-html
- Allure-pytest
- configparser

# 🧪 Selenium UI Automation Framework with PyTest  
### Finexus Home Assessment | Python + Selenium + PyTest + Allure

This is a demo project showcasing my skills in UI test automation using the **Selenium WebDriver** and **PyTest** frameworks, with reporting via **pytest-html** and **Allure**.

---

## 📁 Project Structure

<details>
<summary><strong>Click to expand</strong></summary>

```plaintext
.
├── config/
│   └── config.ini              # Configuration file for credentials and URLs
├── pages/
│   ├── login_page.py           # LoginPage class (Page Object Model)
│   └── secure_area_page.py     # SecureAreaPage class (Page Object Model)
├── tests/
│   └── test_login.py           # Login test case using Page Objects
├── html_reports/               # PyTest HTML reports
├── main.py                     # Entry point to run tests and generate reports
├── conftest.py                 # PyTest fixtures (WebDriver setup/teardown)
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

</details>

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/wan-iqra/Home_Assessment.git
cd Home_Assessment
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment

Edit the `config/config.ini` file:

```ini
[credentials]
email = your_email@example.com
password = your_password

[urls]
login_page = https://your-app.com/login
```

---

## 🧪 Running the Tests

### ▶️ Option 1: Run `main.py` for HTML Reports

- Ensure lines **10–25** in `main.py` are **uncommented**.
- This will:
  - Run all test cases
  - Generate a report in `html_reports/`
  - Automatically open the report in your browser

**Example HTML Report:**

![HTML Report](https://github.com/user-attachments/assets/0e5c4d73-e2f8-4bab-ba32-4b1469c5c1e3)

---

### ▶️ Option 2: Run with Allure Reporting (if installed)

- Ensure lines **29–36** in `main.py` are **uncommented**.
- This will:
  - Run all test cases
  - Generate an **interactive** Allure report in `reports_allure/`
  - Automatically open the report

> 🛠️ Prerequisites:  
> - [Java SDK](https://www.oracle.com/java/technologies/downloads/)  
> - [Allure CLI](https://docs.qameta.io/allure/#_installing_a_commandline)

---

## ⚙️ Installing Allure CLI (via Scoop)

Run the following commands in **PowerShell**:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
iwr -useb get.scoop.sh | iex
scoop install allure
```

Check if Allure is installed:

```bash
allure --version
```

**Allure Report Example:**

![Allure Report](https://github.com/user-attachments/assets/fc3f4db3-da53-4f26-b710-871a1201d0e6)

---

## 🧰 Tools & Technologies

| Tool           | Description                         |
|----------------|-------------------------------------|
| Python 3.8+    | Programming language                |
| Selenium       | Web automation framework            |
| PyTest         | Python test framework               |
| pytest-html    | HTML test report plugin             |
| Allure-pytest  | Allure report plugin for PyTest     |
| configparser   | INI file parsing                    |

---

## ✅ Final Notes

- Screenshots in this README are for illustration only.
- Make sure to update `config.ini` with your actual credentials and URLs.
- If you encounter issues with reports not displaying, ensure dependencies and Java are correctly set up.

---

Happy Testing! 💻🧪

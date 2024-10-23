# Test Automation Template [ Pytest-Playwright-Python ]

This project provides a template for running end-to-end (E2E) tests using Playwright and Pytest in Python.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/downloads/windows/)
- [Playwright](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/en/stable/)
- [JDK](https://www.oracle.com/java/technologies/downloads/#jdk21-windows)
- [Scoop](https://scoop.sh/)
- [Allure](https://allurereport.org/docs/install-for-windows/)

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/alice-labs/playwright_pytest_template.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd playwright-pytest-template
   ```

3. **Install dependencies:**

   Run the following command to install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**

   Playwright requires browser binaries to be installed:

   ```bash
   playwright install
   ```

## Project Structure

The project is organized as follows:

```
    playwright_pytest_template/
    ├─ e2e
    │  ├─ config
    │  │  ├─ example_config.json
    │  │  └─ example_login_data.json
    │  ├─ fixtures
    │  │  └─ setup.py
    │  ├─ pages
    │  │  ├─ __init__.py
    │  │  ├─ chatbox_page.py
    │  │  └─ login_page.py
    |  ├─ tests
    │  │  ├─ __init__.py
    │  │  ├─ base_test.py
    │  │  ├─ chatbox_test.py
    |  |  └─ conftest.py
    |  └─ utils
    │     ├─ __init__.py
    │     └─ config_loader.py
    ├─ .gitignore
    ├─ pytest.ini
    └─ requirements.txt
```

## Configuration

You can configure your own test setup in `setup.py` file.

```code
browser: Browser = playwright.chromium.launch(headless=False, slow_mo=50)     # Browser setup for headed mode and slowmo for slow interaction (Also can set for headless mode for CLI operation)
context: BrowserContext = browser.new_context(no_viewport=True)               # Browser context for maximize window 
```

You must write necessary information in below files:

`config.json`
```code
{
  "base_url": "https://example.com"
}
```

`login_data.json`
```
{
  "user_credentials": {
    "email": "john@example.com",
    "password": "example123!"
  }
}
```
## Running Tests

To run tests with the Playwright fixtures, use:

```bash
pytest                                                     # Run all tests
pytest e2e/tests/chatbox.py                                # Run specific test 
pytest e2e/tests/chatbox.py --browser=chromium             # Specify a browser (Chromium, Firefox, WebKit)
```

You can also use Pytest's options to filter specific tests, run in parallel, etc.

## Test Result

By default, test results will be printed in the console. To generate a Allure reports:

```bash
[pytest]
addopts = --alluredir=./reports --maxfail=3
log_cli = true
log_cli_level = INFO
testpaths = e2e/tests
```
To run the `Allure` report:

`Prerequisites for allure report:`
```bash
System Variable Name : JAVA_HOME
System Variable Value : C:\Program Files\Java\jdk(your version) # Find via browsing

System Variable Name : PATH 
System Variable Value : %JAVA_HOME%\bin
```

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
scoop install allure
allure --version
```

```bash
allure serve reports
```
## Contributing

This template is created by ***[Jayed](https://github.com/jayeeed)*** and ***[Jubair](github.com/Jubair-Ahmed-Khan)***

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

**Run commands in terminal IDE**
1. Install python3
2. python3 -m venv env (create env)
2. source env/bin/activate (activate env)
3. pip install -r requirements.txt (install dependencies from requirements.txt file)
4. pytest tests/test_login.py --alluredir=allure-results (execute test_login.py)

**Test Results**

- Test results will be collected into the following folders:
target/allure-results/xxxxx-xxxxx-test.xml file will contain information about test steps (Allure)

**Clean cache on Ubuntu/OS X systems**
- sudo find . -name \*.pyc -delete

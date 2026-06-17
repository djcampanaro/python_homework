from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("https://owasp.org/www-project-top-ten/")
except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")

sleep(3)
top_10_list = driver.find_element(By.CSS_SELECTOR, '.page-body a')
top_10_list.click()

sleep(2)
vulnerabilities_list = []
navigation_h3 = driver.find_element(By.CSS_SELECTOR, '[id="navigation"]')
if navigation_h3:
    vulnerabilities_sibling = navigation_h3.find_element(By.XPATH, 'following-sibling::ol')
    vulnerabilities = vulnerabilities_sibling.find_elements(By.CSS_SELECTOR, 'li a')
    for vulnerability in vulnerabilities:
        name = vulnerability.text.split('- ')[1]
        print(name)
        link = vulnerability.get_attribute('href')
        if name and link:
            vulnerabilities_list.append({
                "name": name,
                "url": link
            })
print(vulnerabilities_list)

df = pd.DataFrame(vulnerabilities_list)
df.to_csv('owasp_top_10.csv', index=False)

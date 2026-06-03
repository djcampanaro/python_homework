from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

import pandas as pd
import json

## Task 3: Write a Program to Extract this Data

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")

results = []
next_page = True
while next_page:
    book_list_current_page = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')

    for item in book_list_current_page:
        title = item.find_element(By.CSS_SELECTOR, 'span.title-content').text
        authors = [author.text for author in item.find_elements(By.CSS_SELECTOR, 'a.author-link')]

        if len(authors) > 1:
            authors = "; ".join(authors)
        elif len(authors) == 1:
            authors = authors[0]
        else:
            authors = "Unknown"

        format_year = item.find_element(By.CSS_SELECTOR, 'div.cp-format-info span span.display-info-primary').text
        results.append({
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        })

    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'li.pagination__next-chevron a')
    except NoSuchElementException:
        print("No more pages to navigate.")
        next_page = False
    else:
        sleep(2)
        next_button.click()
        sleep(3)

df = pd.DataFrame(results)
print(df)

## Task 4: Write out the Data

df.to_csv('get_books.csv', index=False)
get_books_json = json.dumps(results, indent=4)
with open('get_books.json', 'a') as json_file:
    json_file.write(get_books_json)

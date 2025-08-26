(from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Setup
query = "phones"
os.makedirs('daraz_data', exist_ok=True)
driver = webdriver.Chrome()

# Loop through 5 pages
for page in range(1, 6):
    url = f"https://www.daraz.pk/catalog/?page={page}&q={query}&spm=a2a0e.tm80335142.search.d_go"
    driver.get(url)

    try:
        
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Bm3ON"))
        )

        # Optional: give extra time to load everything
        time.sleep(2)

        # Save the full page HTML
        with open(f'daraz_data/{query}_page{page}.html', mode='w', encoding='utf-8') as file:
            file.write(driver.page_source)

        print(f"Page {page} saved successfully.")

    except Exception as e:
        print(f"Page {page} failed to load: {e}")

# Done
driver.quit()
print("All pages processed.")

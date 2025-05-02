from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Setup Chrome options
options = Options()
# options.headless = True  # Disable for debugging
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Adjust if needed

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Go to the IPL page
    url = 'https://www.iplt20.com/stats/2024/orange-cap'
    driver.get(url)
    time.sleep(5)  # Wait for JS to load

    # Grab table rows
    rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
    data = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        cols = [col.text.strip() for col in cols]
        if cols:
            data.append(cols)

    # Create DataFrame and save
    columns = ['Pos', 'Player', 'Team', 'Matches', 'Innings', 'Runs', 'Average', 'Strike Rate', '100s', '50s', 'Fours', 'Sixes']
    df = pd.DataFrame(data, columns=columns)
    df.to_csv('ipl_2024_orange_cap.csv', index=False)
    print("✅ Data saved successfully.")

except Exception as e:
    print(" Error:", e)

finally:
    driver.quit()

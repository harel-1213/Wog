

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "http://localhost:8777/"

def test_scores_service():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get(URL)

    try:
        # Wait for page to load
        time.sleep(4)

        # Find and extract the score element
        score_element = driver.find_element(By.XPATH, '//*[@id="score"]')
        score = int(score_element.text)

        # Check if the score is within the expected range
        assert 0 < score < 1001, "Score is not within the expected range"

        print("The score is good")
    except Exception as e:
        print("An error occurred:", e)
        raise
    finally:
        # Quit the WebDriver session
        driver.quit()

if __name__ == "__main__":
    test_scores_service()

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json
from card_scraper import scrape_card

driver = webdriver.Chrome(executable_path=r"C:\Users\tickt\Developing\chromedriver.exe")



driver.get("https://en.ws-tcg.com/cardlist/list/")

exp_count = len(driver.find_elements_by_xpath("//div[@id='expansionList']/div/ul/li/a"))
data = []
for i in range(2, exp_count):
    time.sleep(5)
    driver.find_elements_by_xpath("//div[@id='expansionList']/div/ul/li/a")[i].click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'cardno')]"))).click()

    scrape_card(driver)
    while True:
        time.sleep(3)
        try:
            driver.find_element_by_xpath('//p[@class="neighbor"]/span[@class="disable" and contains(text(), "next")]')
            break
        except NoSuchElementException:
            driver.find_element_by_xpath("//p[@class='neighbor']/a[contains(text(), 'next')]").click()
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//table[@class="status"]/tbody/tr/td')))
            data.append(scrape_card(driver))
            continue
    
    with open('set{}.json'.format(i), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        data = []
    
    break
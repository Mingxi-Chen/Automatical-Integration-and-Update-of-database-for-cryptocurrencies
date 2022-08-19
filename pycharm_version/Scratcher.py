# This python file is to use selenium to control the website automatically and assign specific orders to let selenium complete your tasks
# run time can be adjusted case by case
# Author: Mingxi Chen Mx.Chen.official@outlook.com
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


# import csv file
listName = []
with open("csvfile.csv", newline='') as file:
    csv_reader = csv.reader(file, delimiter=',')
    listName = csv_reader.__next__()

# install selenium
driver = webdriver.Chrome('/path/to/chromedriver') 

driver.implicitly_wait(30)

for str in listName[0:10]:
    url = 'data source'
    driver.get(url)

    print(url)
    # locates button: By.XPATH is case by case based your requirements
    element0 = driver.find_element(By.XPATH, '//*[@id="render-target-default"]/div/div[3]')
    element1 = element0.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]')  
    element2 = element1.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div/div') 
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div/div'))).click()
    # click dropdown-menu
    element3 = element2.find_element(By.XPATH, '//*[@id="dropdown-menu"]')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dropdown-menu"]'))).click()


    MAX = element3.find_element(By.XPATH, '//*[@id="dropdown-menu"]/div/ul[2]/li[4]/button')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dropdown-menu"]/div/ul[2]/li[4]/button')))
    MAX.click()
    
    d = driver.find_element(By.CSS_SELECTOR,'a[href*="download"]')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href*="download"]')))
    d.click()
    print('this url is done')
    time.sleep(16)

driver.close()

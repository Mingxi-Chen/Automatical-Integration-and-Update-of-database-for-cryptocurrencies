# This python file aims to catch last 7 days data from yahoo and to match the format of data with master database
# Author: Mingxi Chen Mx.Chen.official@outlook.com

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# import crypto names
listName = []
with open("csvfile.csv", newline='') as file:
    csv_reader = csv.reader(file, delimiter=',')
    listName = csv_reader.__next__()

# transform str to formal date: input str output list with formal date
def transform(str):
    strList = str.split()
    strList[0:3] = [' '.join(strList[0:3])]
    date = strList[0]
    d = datetime.strptime(date, '%b %d, %Y')
    strList[0] = d.strftime('%d/%m/%Y')
    return strList

database = []

driver.implicitly_wait(10)

for str in listName[0:10]:
    url = 'https://finance.yahoo.com/quote/{}-USD/history?p={}-USD'.format(str,str)
    driver.get(url)
    dataList = []
    body = driver.find_element(By.XPATH,'//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody')
    DaysList = body.find_elements(By.CLASS_NAME,'BdT')
    for day in DaysList[0:5]:
        dataList.append(transform(day.text))
    subDataFrame = pd.DataFrame(dataList)
    subDataFrame.insert(0,'Asset',str)
    database.append(subDataFrame)

    time.sleep(8)
driver.close

# final step
df = pd.concat(database)
df.columns =['Asset','Date','Open','High','Low','Close','Adj Close','Volume']
df.to_csv("top10Updated.csv",index=False)


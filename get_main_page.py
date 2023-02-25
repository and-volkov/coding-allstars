import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


driver = webdriver.Firefox()
options = Options()
options.headless = True
options.page_load_strategy = 'eager'

url = 'https://www.classcentral.com/'
file = "/Users/and_volkov/Dev/coding-allstars/downloaded/index.html"
driver.get(url)
time.sleep(30)
pageSource = driver.page_source
fileToWrite = open(file, "w")
fileToWrite.write(pageSource)
fileToWrite.close()
fileToRead = open(file, "r")
print(fileToRead.read())
fileToRead.close()
driver.quit()

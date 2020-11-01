from selenium import webdriver
import requests
import time

response = requests.get("https://xrohan.me/proxy")

proxy = response.text


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--allow-popups-during-page-unload")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--enable-auto-reload")
chrome_options.add_argument(f'--proxy-server={proxy}')


driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)

driver.get("https://www.alexamaster.net/ads/autosurf/117735")

time.sleep(600)


driver.quit()

from selenium import webdriver
import requests
import time


def first():
  response = requests.get("https://xrohan.me/proxy")

  proxy = response.text


  chrome_options = webdriver.ChromeOptions()
  #chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--allow-popups-during-page-unload")
  chrome_options.add_argument("--disable-popup-blocking")
  chrome_options.add_argument("--enable-auto-reload")
  chrome_options.add_argument(f'--proxy-server={proxy}')

  driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
  driver.get("https://google.com")

  try:
    print(driver.title)
  except:
    driver.quit()
    first()

first()
time.sleep(3)
driver.get("https://url.rw/?https%3A%2F%2Ft.co%2FWV8SaGbYLi%3Famp%3D1")
time.sleep(23)
driver.refresh()
time.sleep(60)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)
driver.refresh()
time.sleep(120)




driver.quit()

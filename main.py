from selenium import webdriver
import requests
import time


def first():
  global driver
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

  youtube()



def youtube():
  try:
    driver.set_page_load_timeout(30)
    driver.get("https://youtube.com")
    print(driver.title)
  except:
    driver.quit()
    first()


def ws():
  driver.get("http://www.websurf.cz/auto/?name=rock6064")
  time.sleep(120)


def ws2():
  global sm
  sm = 0
  while sm != 20:
    try:
      ws()
      sm += 1
    except:
      driver.quit()
      first()
      sm += 1








first()
ws2


driver.quit()

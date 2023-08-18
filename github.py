from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

url="https://google.com/"

driver.get(url)
print(f"şuanki url:{driver.current_url}")
print(f"şuanki title:{driver.title}")
# driver.save_screenshot("github.png")
aramaKutusu=driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
aramaKutusu.send_keys("example selenium")

aramaKutusu.send_keys(Keys.ENTER)


time.sleep(2)
# driver.quit()
# driver.close()
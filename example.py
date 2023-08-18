from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

# url="https://google.com/"
# driver.get(url)
# print(f"şuanki url:{driver.current_url}")
# print(f"şuanki title:{driver.title}")
# # driver.save_screenshot("github.png")
# aramaKutusu=driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
# aramaKutusu.send_keys("example selenium") #veri girme
# aramaKutusu.send_keys(Keys.ENTER)    #enter tuşuna basma


# url="https://tr.wikipedia.org/wiki/Anasayfa"
# driver.get(url)
# baslik=driver.find_element(By.ID,'mp-tfa-h2')
# metin=driver.find_element(By.ID,'mp-tfa')
# print(baslik.text)
# print(metin.text)

# url="https://the-internet.herokuapp.com/login"
# driver.get(url)
# username=driver.find_element(By.NAME,'username')
# password=driver.find_element(By.NAME,'password')
# loginButton=driver.find_element(By.XPATH,'//*[@id="login"]/button')
# #login
# username.send_keys("tomsmith")
# password.send_keys("SuperSecretPassword!")
# #password.send_keys(Keys.ENTER)
# time.sleep(1)
# loginButton.click()
# time.sleep(1)
# mesaj =driver.find_element(By.ID,'flash').text
# if "Your username is invalid!" in mesaj:
#     print("kullanıcı adı hatalı")
#     print("işlem başarısız")
# elif "Your password is invalid!" in mesaj:
#     print("Parola hatalı")
#     print("işlem başarısız")
# elif driver.current_url== "https://the-internet.herokuapp.com/secure":
#     if "You logged into a secure area!" in mesaj:
#         safearea=driver.find_element(By.XPATH,'//*[@id="content"]/div/h2')
#         if "Secure Area" in safearea.text:
#             print("giriş başarılı")
# else :
#     print("else:işlem başarısız")
    



time.sleep(1)
driver.quit()
# driver.close()
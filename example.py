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
    
#IMDb Top 250 Movies
# url="https://www.imdb.com/"
# driver.get(url)
# menuButton=driver.find_element(By.XPATH,'//*[@id="imdbHeader-navDrawerOpen"]')
# menuButton.click()
# top250=driver.find_element(By.XPATH,'//*[@id="imdbHeader-navDrawer"]/div/div[2]/div/div[1]/span/div/div/ul/a[2]/span')
# top250.click()
# time.sleep(1)
# filmler=driver.find_elements(By.XPATH,'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[@class="ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent"]')
# time.sleep(1)
# for i in filmler:
#     print(i.find_element(By.XPATH,'div[2]/div/div/div[1]/a/h3').text)

url="https://tomspizzeria.b4a.app/"
driver.get(url)
time.sleep(1)
musteriAdi=driver.find_element(By.ID,'musteri-adi').send_keys("mehmet")
pizzaBoyu=driver.find_element(By.XPATH,'//*[@id="select-size"]/div/div/div[1]/input')
if pizzaBoyu.is_selected() == False:
    pizzaBoyu.click()

pizzaEkle=driver.find_element(By.XPATH,'//*[@id="select-topping"]/div/div/div[1]/input').click()
pizzaOdeme=driver.find_element(By.XPATH,'//*[@id="odeme-tipi"]')
pizzaOdeme.click()
pizzaOdemeNakit=driver.find_element(By.XPATH,'//*[@id="odeme-tipi"]/option[2]')
pizzaOdemeNakit.click()

siparisButton=driver.find_element(By.ID,'siparis')
if siparisButton.is_displayed()==False:
    print("hata: aktif değil basılmıyor ")
else:
    siparisButton.click()




time.sleep(1)
driver.quit()
# driver.close()
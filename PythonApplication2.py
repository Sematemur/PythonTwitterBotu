from selenium.webdriver.common.by import By
from bilgi import isim, sifre,hashtag
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
class Twitter:
    def __init__(self,isim,sifre):
                yol = "C:\\Users\\SEMA\\Downloads\\chromedriver_win32\\chromedriver.exe"
                self.driver = webdriver.Chrome(yol)
                self.isim = isim
                self.sifre = sifre
                time.sleep(3)
    def girisyapma(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(4)
        isimyolu=self.driver.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        isimyolu.send_keys(self.isim)
        isimyolu.send_keys(Keys.ENTER)
        time.sleep(2)
        sifreyolu=self.driver.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        sifreyolu.send_keys(self.sifre)
        time.sleep(3)
        sifreyolu.send_keys(Keys.ENTER)
        time.sleep(3)
    def bildirimlerig�sterme(self):
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[3]").click()
        time.sleep(3)
    def mesajlarig�sterme (self):
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[4]").click()
        time.sleep(4)
    def hastaghg�rearama(self,hashtag):
        self.hashtag=hashtag
        arama=self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
        arama.send_keys(self.hashtag)
        arama.send_keys(Keys.ENTER)
        time.sleep(4)
    def takipetme(self):
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div").click()
        time.sleep(3)




twitter=Twitter(isim,sifre)
twitter.girisyapma()
twitter.mesajlarig�sterme()
twitter.bildirimlerig�sterme()
twitter.hastaghg�rearama(hashtag)
twitter.takipetme()


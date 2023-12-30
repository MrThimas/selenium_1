from selenium import webdriver
import time

navegador = webdriver.Chrome()

navegador.get('https://ri.magazineluiza.com.br/')
navegador.find_element('xpath', '//*[@id="Form1"]/header/div/div/div/div[1]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="heading-mobile-3"]/button').click()
time.sleep(5)
navegador.find_element('xpath', '//*[@id="collapse-mobile-3"]/div/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element('xpath', '//*[@id="LCT0jcMkm6vLyEUX8g5eiA=="]').click()
time.sleep(5)
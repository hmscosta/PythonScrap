from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
import csv
import time


class Linkedin:

    email = ""
    password = ""
    LOGGER.setLevel(logging.WARNING)
    credenciais = open("/home/henrique/Documents/Henrique/lkbot","r") #Arquivo que contem as credencias de acesso

    #Metodo para ler as creencias salvas em um arquivo externo
    def lerCredenciais(self):
        spamreader = csv.reader(self.credenciais, delimiter=',')
        for row in spamreader:
            self.email = row[0]
            self.password = row[1]
        self.credenciais.close()
        
    #Metodo que cuida do login
    def login(self):
        binary = FirefoxBinary('/usr/bin/firefox')
        driver = webdriver.Firefox(firefox_binary=binary)
        driver.get('https://www.linkedin.com/')
        emailBar = driver.find_element_by_id("session_key")
        passwordBar = driver.find_element_by_id("session_password")
        emailBar.clear()
        passwordBar.clear()
        emailBar.send_keys(self.email)
        passwordBar.send_keys(self.password)
        passwordBar.send_keys(Keys.RETURN)
        print("TITULO - %s" % driver.title)
        time.sleep(10)
        driver.get("https://www.linkedin.com/search/results/content/?facetSortBy=date_posted&keywords=oportunidade de trabalho&origin=SORT_RESULTS")
        time.sleep(2)
        #textoDoCartao = driver.find_elements_by_class_name("break-words")
        #elementList = textoDoCartao[0].find_elements_by_tag_name("span")
        #print(driver.find_element_by_css_selector("span.break-words > span").get_attribute('innerHTML'))
        print(driver.find_element_by_css_selector("span.break-words > span").get_attribute('innerText'))
        print("----------")
        #print(driver.find_elements_by_xpath("(//span[@class='break-words'])/span[0]").get_attribute('innerText'))
        #driver.quit()

    def printar(self):
        print("CLASSE LINKEDIN")


    def testes(self):
        binary = FirefoxBinary('/usr/bin/firefox')
        driver = webdriver.Firefox(firefox_binary=binary)
        driver.get('https://www.google.com/')
        time.sleep(10)
        driver.get('https://www.youtube.com/')



  
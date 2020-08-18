from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
import csv

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
        #driver.quit()

    def printar(self):
        print("CLASSE LINKEDIN")


  
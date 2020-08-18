from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class Linkedin:


    def login(self):
        binary = FirefoxBinary('/usr/bin/firefox')
        browser = webdriver.Firefox(firefox_binary=binary)
        browser.get('https://www.linkedin.com/')
        

    def printar(self):
        print("CLASSE LINKEDIN")
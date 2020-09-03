import scrapy
from scrapy.crawler import CrawlerProcess
from Spyders.WebSpyder import WebSpyder
from Spyders.ImageSpyder import ImageSpyder
from Spyders.AranhaIndustrial import AranhaIndustrial
from Spyders.AranhaLinkedin import AranhaLinkedin
from Spyders.VagasPontoCom import VagasPontoCom
from Spyders.AranhaProfissoes import AranhaProfissoes
from Selen.Linkedin import Linkedin
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import json

class Program:

    def main():
        #y = []
        #arquivo = open('data.json', 'a')
        print("Metodo MAIN")
        process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        
        runner = CrawlerRunner()
        d = runner.crawl(VagasPontoCom)
        reactor.run() # the script will block here until the crawling is finished
        print("Finalizando.......")
        #y.append({"descricaoVaga":'Nikhil', 
        # "tagVaga": "nikhil@geeksforgeeks.org", 
        # "TituloVaga": "Full Time"
        #})
        #print(y)
        #json.dump(y, arquivo)
        #arquivo.close()

        #objetoLinkedin = Linkedin()
        #objetoLinkedin.lerCredenciais()
        #objetoLinkedin.login()
        

    
    if __name__ == "__main__":
        main()
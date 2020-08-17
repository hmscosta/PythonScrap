
import scrapy
from scrapy import signals
from twisted.internet import reactor
import json

class AranhaLinkedin(scrapy.Spider):

    name = 'aranha_linkedin'
    start_urls = [  #Metodo simplificado de usar a aranha, define somente a lista com o nome start_urls e nao precisa usar o loop for
        'https://www.cadastroindustrialmg.com.br:449/industria/setor'
    ]
    
    def close(self, reason):
        print("ARANHA FECHADA")
        reactor.stop()


    #Metodo inical da aranha sera chado primeiro
    def start_requests(self):
        url = "https://www.cadastroindustrialmg.com.br:449/Industria/Setor"
        headers= {'Accept':'*/*'} 
        i = "24"
        payload = {"id": str(i)}
        yield scrapy.FormRequest(url, 
                            formdata = payload,
                            method='POST',
                            callback = self.parse)


    def parse(self, response):
        print("------------%s trabalhando------------------" % self.name)
    
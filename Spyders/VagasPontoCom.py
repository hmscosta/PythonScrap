import scrapy
from scrapy import signals
from Moeda import Moeda
from twisted.internet import reactor
import json

class VagasPontoCom(scrapy.Spider):
    
    name = 'aranha_vagas'
    nextUrls = []
    arquivo = open("texto/vagas.txt","a")

    def close(self, reason):
        print(" %s fechada "% self.name)
        self.arquivo.close()
        reactor.stop()
  
    def getVaga(self,response):
        tituloDaVaga = response.css("h1::text").get()
        beneficiosDaVaga = response.css("span.benefit-label::text").getall()
        descricaoDaVaga = response.css("div.job-tab-content.job-description__text.texto p::text").getall()
        self.arquivo.write("%s \n %s \n %s \n -------------------------------------------- "   % (tituloDaVaga, beneficiosDaVaga, descricaoDaVaga) )  


    #Metodo de retorno da request da aranha no primeiro nivel
    def menuPrimeiroNivel(self, response):
        titulo = response.css("h2::text").get()
        if(titulo == 'Não encontramos vagas'):
            return        
        else:
            self.nextUrls = response.css("h2.cargo a::attr(href)").getall()
            while( (len(self.nextUrls)) > 0):
                urlDaVaga = "https://www.vagas.com.br"
                urlDaVaga = urlDaVaga + self.nextUrls[0]
                yield scrapy.Request(urlDaVaga, callback=self.getVaga)
                self.nextUrls.pop(0)
            return

    #Metodo inical da aranha sera chado primeiro
    def start_requests(self):
        for i in range(1, 100):
            url = "https://www.vagas.com.br/vagas-de-desenvolvedor?&q=desenvolvedor&pagina=" + str(i)
            yield scrapy.Request(url, callback=self.menuPrimeiroNivel)
         

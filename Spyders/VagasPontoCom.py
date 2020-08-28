import scrapy
from scrapy import signals
from Moeda import Moeda
from twisted.internet import reactor
import json

class VagasPontoCom(scrapy.Spider):
    
    name = 'aranha_vagas'
    nextUrls = []
    arquivo = open("texto/vagas.json","a")
    vaga = []

    def close(self, reason):
        print(" %s fechada "% self.name)
        json.dump(self.vaga, self.arquivo)
        print(self.vaga)
        self.arquivo.close()
        reactor.stop()
  
    def getVaga(self,response):
        beneficios = ""
        vagaDescrita = ""
        tituloDaVaga = response.css("h1::text").get()
        tituloDaVaga = tituloDaVaga.replace('\n', '')
        tituloDaVaga = tituloDaVaga.lstrip()
        tituloDaVaga = tituloDaVaga.rstrip()
        beneficiosDaVaga = response.css("span.benefit-label::text").getall()
        descricaoDaVaga = response.css("div.job-tab-content.job-description__text.texto p::text").getall()
        for benVaga in beneficiosDaVaga:
            beneficios = beneficios + benVaga + ","
        for descVaga in descricaoDaVaga:
            vagaDescrita = vagaDescrita + descVaga + ","
        vagaDescrita = vagaDescrita.replace(u'\xa0', u' ')    
        vagaCompleta = tituloDaVaga + "," + vagaDescrita + "," + beneficios
        #vagaCompleta = vagaCompleta.encode('latin-1','ignore')
        self.vaga.append({"descricaoVaga": vagaCompleta, 
         "tagVaga": "desenvolvedor", 
         "TituloVaga": tituloDaVaga
        })
        


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
         

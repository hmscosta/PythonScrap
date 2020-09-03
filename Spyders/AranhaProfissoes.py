
import scrapy
from scrapy import signals
from twisted.internet import reactor
import json
import string

class AranhaProfissoes(scrapy.Spider):

    name = 'aranha_profissoes'
    nextUrls = []
    arquivo = open("texto/profissoes.json","a")
    profissao = []

    def close(self, reason):
        print(" %s fechada "% self.name)
        #print(self.profissao[0])
        for linha in self.profissao:
            self.arquivo.write(linha + ",")
        self.arquivo.close()
        #print(self.profissao)
        reactor.stop()



    #Metodo de retorno da request da aranha no primeiro nivel
    def menuPrimeiroNivel(self, response):
            lista = response.css("div.Col-o5r7t1-0.List__ProfessionsChunk-sc-1akqnzm-3.kUNwlr a::text").getall()
            for entrada in lista:
                self.profissao.append(entrada)
            return



    #Metodo inical da aranha sera chado primeiro
    def start_requests(self):
        for i in range(0, 26):
            url = "https://www.catho.com.br/profissoes/cargo/" + string.ascii_lowercase[i]
            yield scrapy.Request(url, callback=self.menuPrimeiroNivel)
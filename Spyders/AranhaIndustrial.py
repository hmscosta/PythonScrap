
import scrapy
from Moeda import Moeda
from twisted.internet import reactor


class AranhaIndustrial(scrapy.Spider):

    name = 'aranha_industrial'
    start_urls = [  #Metodo simplificado de usar a aranha, define somente a lista com o nome start_urls e nao precisa usar o loop for
        'https://www.cadastroindustrialmg.com.br:449/industria/setor'
    ]
    
    def start_requests(self):
        url = "https://www.cadastroindustrialmg.com.br:449/Industria/Setor"
        headers= {'Accept':'*/*'} 
        payload = {"id": "24"}
        return [scrapy.FormRequest(url, 
                        formdata = payload)]
    
  
    #def parse(self, response):
    #    page = response.url
    #    print("------------%s trabalhando------------------" % self.name)
    #    url = "https://www.cadastroindustrialmg.com.br:449/Industria/Setor"
    #    headers= {'Accept':'*/*'} 
    #    payload = {"id": "24"}
    #    retornado = yield scrapy.FormRequest( url, 
    #                    formdata = payload)
        
        
        #setores = response.css("div.setor-nome p::text").getall()
        #for i in range(len(setores)):
        #    print("%s " % setores[i])
        #print("------------------------------")
        
        #next_page = response.css("li.next a::attr(href)").get()  #Pega a url da proxima pagina
        #if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse) #Faz um novo request para a aranha 
        #else:
        #    reactor.stop() #Desbloqueia a thread
        #reactor.stop() 

       #https://www.cadastroindustrialmg.com.br:449/industria/resultadobusca?Filters=Setor:SUBMENU;&K=NOME_DA_PRIMEIRA_PALAVRA_DO_SUBMENU
        
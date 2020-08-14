
import scrapy
from Moeda import Moeda
from twisted.internet import reactor
import json

#Aranha que vai fazer o scrapping no site do cadastro industrial
class AranhaIndustrial(scrapy.Spider):

    name = 'aranha_industrial'
    start_urls = [  #Metodo simplificado de usar a aranha, define somente a lista com o nome start_urls e nao precisa usar o loop for
        'https://www.cadastroindustrialmg.com.br:449/industria/setor'
    ]
    
    #Metido de retorno da request da aranha
    def retornoRequest(self, response):
        resp_dict = json.loads(response.body)
        retorno = resp_dict
        lista = retorno[0].get('subCategoria')
        print(lista)
        print("----------------------------------------------")
        #print(lista[0])
        #print(lista[0].get('Nome'))
        for nomes in lista:
            print(nomes.get('Nome'))

        #resp_dict['value']['queryInfo']['creationTime'] # 1349724919000
        reactor.stop()

    #Metodi inical da aranha sera chado primeiro
    def start_requests(self):
        url = "https://www.cadastroindustrialmg.com.br:449/Industria/Setor"
        headers= {'Accept':'*/*'} 
        payload = {"id": "24"}
        yield scrapy.FormRequest(url, 
                        formdata = payload,
                        method='POST',
                        callback = self.retornoRequest)
    
  
    #def parse(self, response):
    #    page = response.url
    #    print("------------%s trabalhando------------------" % self.name)
    #    print(response)
    #    url = "https://www.cadastroindustrialmg.com.br:449/Industria/Setor"
    #    headers= {'Accept':'*/*'} 
    #    payload = {"id": "24"}
    #    retornado = yield scrapy.FormRequest( url, 
    #                    formdata = payload)
        
        
        #setores = response.css("div.setor-nome p::text").getall()
        #for i in range(len(setores)):
        #    print("%s " % setores[i])
       
        
        #next_page = response.css("li.next a::attr(href)").get()  #Pega a url da proxima pagina
        #if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse) #Faz um novo request para a aranha 
        #else:
        #    reactor.stop() #Desbloqueia a thread
        #reactor.stop() 

       #https://www.cadastroindustrialmg.com.br:449/industria/resultadobusca?Filters=Setor:SUBMENU;&K=NOME_DA_PRIMEIRA_PALAVRA_DO_SUBMENU
        
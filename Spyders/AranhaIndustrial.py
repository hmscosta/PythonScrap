
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
    
    #Metodo para desbloquear a thread
    def desligarAranha(self):
        reactor.stop()
    
    #Metodo de retorno da request da aranha no segundo nivel
    def menuSegundoNivel(self, response):
        print("MENU SEGUNDO NIVEL")
        print(response.url)
        self.desligarAranha()


    #Metodo de retorno da request da aranha no primeiro nivel
    def menuPrimeiroNivel(self, response):
        subcategorias = []
        resp_dict = json.loads(response.body)
        retorno = resp_dict
        lista = retorno[0].get('subCategoria')
        print("----------------------------------------------")
        for nomes in lista:
            subcategorias.append(nomes.get('Nome'))
        print(subcategorias)
        print(subcategorias[0])
        print(subcategorias[1])
        print(subcategorias[2])
        print("----------------------------------------------")
        print(subcategorias[0].split(' ', 1)[0])
        print(subcategorias[1].split(' ', 1)[0])
        print(subcategorias[2].split(' ', 1)[0])
        
        ## Montar novo request
        urlSegundoNivel = "https://www.cadastroindustrialmg.com.br:449/industria/resultadobusca?Filters=Setor:" + subcategorias[0] + ";&K="+  subcategorias[2].split(' ', 1)[0]
        #print(urlSegundoNivel)
        next_page = response.urljoin(urlSegundoNivel)
        yield scrapy.Request(next_page, callback=self.menuSegundoNivel) #Faz um novo request para a aranha 

        #yield scrapy.Request(self.start_urls[0], callback=self.menuSegundoNivel) #Faz um novo request para a aranha 
        #yield scrapy.Request(self.start_urls[0], callback=self.parse) #Faz um novo request para a aranha 

        #self.desligarAranha()

    #Metodo inical da aranha sera chado primeiro
    def start_requests(self):
        url = "https://www.cadastroindustrialmg.com.br:449/Industria/Setor"
        headers= {'Accept':'*/*'} 
        payload = {"id": "24"}
        yield scrapy.FormRequest(url, 
                        formdata = payload,
                        method='POST',
                        callback = self.menuPrimeiroNivel)
    
  
    def parse(self, response):
        #page = response.url
        print("------------%s trabalhando------------------" % self.name)
        self.desligarAranha()
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
        

import scrapy
from scrapy import signals
from Moeda import Moeda
from twisted.internet import reactor
import json

#Aranha que vai fazer o scrapping no site do cadastro industrial
class AranhaIndustrial(scrapy.Spider):

    name = 'aranha_industrial'
    start_urls = [  #Metodo simplificado de usar a aranha, define somente a lista com o nome start_urls e nao precisa usar o loop for
        'https://www.cadastroindustrialmg.com.br:449/industria/setor'
    ]
    urlTerceiroNivel = "https://www.cadastroindustrialmg.com.br:449"    
    urls = []
    urlsSubnivel = []

    def close(self, reason):
        print("ARANHA FECHADA 2")
        reactor.stop()


    #Metodo para desbloquear a thread
    def desligarAranha(self):
        reactor.stop()
    
    def linksSubmenus(self, response):
        self.urlsSubnivel = response.css("a.page-link::attr(href)").getall()
        print("URLS: ")
        self.urlsSubnivel = list( dict.fromkeys(self.urlsSubnivel) )
        print(self.urlsSubnivel)
        urlSegundoNivel = "https://www.cadastroindustrialmg.com.br:449"
        while len(self.urlsSubnivel) > 0:
            next_page = response.urljoin(urlSegundoNivel + self.urlsSubnivel[0])
            yield scrapy.Request(next_page, callback=self.menuSegundoNivel) #Faz um novo request para a aranha 
            self.urlsSubnivel.pop(0)
            


    #Metodo de retorno da request da aranha no segundo nivel
    #Neste nivel estao as informacoes das empresas
    def menuTerceiroNivel(self, response):
        nome = response.css("div.descricao::text").get() #Retorna o nome da empresa
        siteEmail = response.css("div.links a::text").getall()  #Retorna o site e o email
        telefones = response.css("div.contato span::text").getall() #Retorna o telefone
        informacoes = response.css("div.info p::text").getall() # 0- setor de atividade, 1- produtos e servicos, 2- porte
        endereco = response.css("div.endereco::text").getall() #Retorna o endereco
        print("----------------------")
        print(nome)
        print(siteEmail)
        print(telefones)
        print(informacoes)
        print(endereco)
        print("----------------------")

    #Metodo de retorno da request da aranha no segundo nivel
    def menuSegundoNivel(self, response):
        #print("MENU SEGUNDO NIVEL")
        #print(response.url)
        self.urls = response.css("ul.empresas a::attr(href)").getall()
        while len(self.urls) > 0:
            next_page = response.urljoin(self.urlTerceiroNivel + self.urls[0])
            yield scrapy.Request(next_page, callback=self.menuTerceiroNivel) #Faz um novo request para a aranha
            self.urls.pop(0)
       

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
        # Montar novo request
        urlSegundoNivel = "https://www.cadastroindustrialmg.com.br:449/industria/resultadobusca?Filters=Setor:" + subcategorias[0] + ";&K="+  subcategorias[2].split(' ', 1)[0]
        next_page = response.urljoin(urlSegundoNivel)
        #Fazer request para buscar o numero de paginas
        yield scrapy.Request(next_page, callback=self.linksSubmenus)

        #while(len(urlsSubnivel) > 0):
        #    urlSegundoNivel = "https://www.cadastroindustrialmg.com.br:449/industria/resultadobusca?Filters=Setor:" + subcategorias[0] + ";&K="+  subcategorias[2].split(' ', 1)[0]
        #    next_page = response.urljoin(urlSegundoNivel)
        #    yield scrapy.Request(next_page, callback=self.menuSegundoNivel) #Faz um novo request para a aranha 


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
        

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
    subcategorias = []
    arquivo = open("texto/industrias.txt","a")

    def close(self, reason):
        print("ARANHA FECHADA 2")
        self.arquivo.close()
        reactor.stop()


    #Metodo para desbloquear a thread
    def desligarAranha(self):
        reactor.stop()
    
    def linksSubmenus(self, response):
        self.urlsSubnivel = response.css("a.page-link::attr(href)").getall()
        #print("URLS: ")
        self.urlsSubnivel = list( dict.fromkeys(self.urlsSubnivel) )
        #print(self.urlsSubnivel)
        urlSegundoNivel = "https://www.cadastroindustrialmg.com.br:449"
        if(len(self.urlsSubnivel) != 0):
            while len(self.urlsSubnivel) > 0:
                next_page = response.urljoin(urlSegundoNivel + self.urlsSubnivel[0])
                yield scrapy.Request(next_page, callback=self.menuSegundoNivel) #Faz um novo request para a aranha 
                self.urlsSubnivel.pop(0)
        else:
            yield scrapy.Request(response.url, callback=self.menuSegundoNivel) #Faz um novo request para a aranha         
            


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
        self.arquivo.write("%s \n %s \n %s \n %s \n %s \n "   % (nome, siteEmail, telefones, informacoes, endereco))  
        

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
        resp_dict = json.loads(response.body)
        retorno = resp_dict
        lista = retorno[0].get('subCategoria')
        if(len(lista) > 0):
            for nomes in lista:
                self.subcategorias.append(nomes.get('Nome'))
            # Montar novo request
            urlSegundoNivel = "https://www.cadastroindustrialmg.com.br:449/industria/resultadobusca?Filters=Setor:"
            next_page = response.urljoin(urlSegundoNivel)
            #Fazer request para buscar o numero de paginas
            while(len(self.subcategorias) > 0):
                next_page = response.urljoin(urlSegundoNivel + self.subcategorias[0] + ";&K="+  self.subcategorias[0].split(' ', 1)[0])
                yield scrapy.Request(next_page, callback=self.linksSubmenus)
                self.subcategorias.pop(0)
        else:
            return

    #Metodo inical da aranha sera chado primeiro
    def start_requests(self):
        url = "https://www.cadastroindustrialmg.com.br:449/Industria/Setor"
        headers= {'Accept':'*/*'} 
        
        for i in range(100):
            payload = {"id": str(i)}
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
        
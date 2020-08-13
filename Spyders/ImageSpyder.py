
import scrapy
from Moeda import Moeda
from twisted.internet import reactor

class ImageSpyder(scrapy.Spider):

    name = 'aranha_de_imagens'
    start_urls = [  #Metodo simplificado de usar a aranha, define somente a lista com o nome start_urls e nao precisa usar o loop for
        'http://books.toscrape.com/'
    ]
    
    objetoMoeda = Moeda()

    def parse(self, response):
        page = response.url
        print("------------%s trabalhando------------------" % self.name)
        livros = response.css("a::attr(title)").getall()
        precos = response.css("p.price_color::text").getall()
        print("SIZE OF LIVROS: " + str(len(livros)))
        print("SIZE OF PRECOS: " + str(len(precos)))
        arquivo = open("texto/livros.txt","a")
        for i in range(len(livros)):
            print("R$%.2f -- %s"   % (float(self.objetoMoeda.converterMoeda(precos[i], 'GBP', 'BRL')) , livros[i]))
            #arquivo.write("R$%.2f -- %s \n"   % (float(self.objetoMoeda.converterMoeda(precos[i], 'GBP', 'BRL')) , livros[i]))  
            #print(response.css("p.instock availability::text").getall())
        arquivo.close()
        print("------------------------------")
        #next_page = response.css("li.next a::attr(href)").get()  #Pega a url da proxima pagina
        #if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse) #Faz um novo request para a aranha 
        #else:
        #    reactor.stop() #Desbloqueia a thread
        reactor.stop() 
    
    def testes(self):
        print("------------------------------")
        print("TESTANDO ARANHA")
        print("------------------------------")
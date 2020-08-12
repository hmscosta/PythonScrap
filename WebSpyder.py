
import scrapy



class WebSpyder(scrapy.Spider):

    name = 'aranha'
    start_urls = [  #Metodo simplificado de usar a aranha, define somente a lista com o nome start_urls e nao precisa usar o loop for
        'http://books.toscrape.com/'
    ]



    def parse(self, response):
        page = response.url
        print("------------------------------")
        livros = response.css("a::attr(title)").getall()
        precos = response.css("p.price_color::text").getall()
        #print(livros)
        #print(precos)
        print("SIZE OF LIVROS: " + str(len(livros)))
        print("SIZE OF PRECOS: " + str(len(precos)))
        for i in range(len(livros)):
            print(precos[i]  + " -- " + livros[i])  
        #print(response.css("p.instock availability::text").getall())
        #print("Nome do site: "+ page)
        #print("Nome do site: "+ page.split("//")[1])
        print("------------------------------")
        next_page = response.css("li.next a::attr(href)").get()  #Pega a url da proxima pagina
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse) #Faz um novo request para a aranha 

    def testes(self):
        print("------------------------------")
        print("TESTANDO ARANHA")
        print("------------------------------")
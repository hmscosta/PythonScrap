
import scrapy

class Program(scrapy.Spider):

    name = 'aranha'
    start_urls = [  #Metodo simplificado de usar a aranha, define somente a lista com o nome start_urls e nao precisa usar o loop for
        'http://books.toscrape.com/'
    ]

    def main():
        print("Metodo MAIN")
        #objetoPagina = open("pagina.html")
        #objetoPagina.close()


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

    if __name__ == "__main__":
        main()
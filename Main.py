
import scrapy

class Program(scrapy.Spider):

    name = 'aranha'
    start_urls = [  #Metodo simplificado de usar a aranha, define somente a lista com o nome start_urls e nao precisa usar o loop for
        'http://quotes.toscrape.com/tag/humor/',
        'https://docs.scrapy.org/en/latest/intro/tutorial.html'
    ]

    def main():
        print("Metodo MAIN")
        #objetoPagina = open("pagina.html")
        #objetoPagina.close()


    def parse(self, response):
        page = response.url
        print("------------------------------")
        print("Nome do site: "+ page)
        print("Nome do site: "+ page.split("//")[1])
        print("------------------------------")

    if __name__ == "__main__":
        main()
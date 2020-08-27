import scrapy
from scrapy import signals
from Moeda import Moeda
from twisted.internet import reactor
import json

class VagasPontoCom(scrapy.Spider):
    
    name = 'aranha_vagas'

    def close(self, reason):
        print(" %s fechada "% self.name)
        reactor.stop()


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
        url = "https://www.vagas.com.br/vagas-de-desenvolvedor-de-software"
         


from currency_converter import CurrencyConverter

class Moeda:


    def converterMoeda(self,valor, moedaInicial, moedaConvertida):
        c = CurrencyConverter()
        #resultado = c.convert(valor, moedaInicial, moedaConvertida)
        resultado = c.convert(valor[1:], moedaInicial, moedaConvertida)
        return resultado

    #print("testeeeee")
    #print("R$" + "%.2f" % float(converterMoeda(100.1, 'GBP', 'BRL')) )

import json
from ClassesObjeto.Vaga import Vaga
class ClasseTeste:

    vagas = []


    #stringOriginal = "Extra\u00e7\u00e3o e envio de relat\u00f3rios para cliente e opera\u00e7\u00f5es"
    #print(stringOriginal)
    file_path = "/home/henrique/Documents/Desenvolvimento/Python/Aprendizado/PythonScrap/texto/vagas.json"
    arquivo = open(file_path,"r")
    for line in arquivo:
        #print(line)
        review = json.loads(line)
        for cont in range(len(review)):
            #print(cont)
            #print(review[cont]['descricaoVaga'])
            vagas.append(Vaga(review[cont]['descricaoVaga'], review[cont]['tagVaga']))
        #print(review[0]['descricaoVaga'])
        #print(review[0]['tagVaga'])
        #vagas.append(Vaga(review['descricaoVaga'], review['tagVaga']))
    arquivo.close()

    print(vagas[0].descricao)
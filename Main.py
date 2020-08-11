from bs4 import BeautifulSoup


class Program:

    def main():
        print("Teste")
        objetoPagina = open("pagina.html")
        soup = BeautifulSoup(objetoPagina, 'html.parser')
        print(soup.title)
        print(soup.title.name)
        print(soup.title.string)
        print(soup.p)
        print(soup.p.string)
        objetoPagina.close()


    if __name__ == "__main__":
        main()
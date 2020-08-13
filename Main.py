import scrapy
from scrapy.crawler import CrawlerProcess
from Spyders.WebSpyder import WebSpyder
from Spyders.ImageSpyder import ImageSpyder
from Spyders.AranhaIndustrial import AranhaIndustrial
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
import sys

class Program:

    def main():
        print("Metodo MAIN")
        process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        runner = CrawlerRunner()
        d = runner.crawl(AranhaIndustrial)
        reactor.run() # the script will block here until the crawling is finished
        print("Finalizando.......")
        #sys.exit()
    
    if __name__ == "__main__":
        main()
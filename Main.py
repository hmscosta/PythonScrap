import scrapy
from scrapy.crawler import CrawlerProcess
from WebSpyder import WebSpyder
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
import sys

class Program:

    def main():
        print("Metodo MAIN")
        process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        MySpider = WebSpyder()
        runner = CrawlerRunner()
        d = runner.crawl(WebSpyder)
        reactor.run() # the script will block here until the crawling is finished
        print("Finalizando.......")
        #sys.exit()
    
    if __name__ == "__main__":
        main()
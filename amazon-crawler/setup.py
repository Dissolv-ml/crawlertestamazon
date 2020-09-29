from scrapy.crawler import CrawlerProcess
from .spiders import amazon_scraper
process = CrawlerProcess()
process.crawl(amazon_scraper)
process.start()



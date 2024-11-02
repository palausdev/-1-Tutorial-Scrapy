import scrapy


class LiberiaCrawlSpider(scrapy.Spider):
    name = "liberia-crawl"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        xpath_title = './/a//@title'
        xpath_price = './/div[contains(@class, "product_price")]//p[1]//text()'
        xpath_is_boolean = './/p[contains(@class, "instock")]//i[contains(@class, "ok")]'
        
        books = response.xpath('//article[contains(@class, "product_pod")]')
        for book in books:
            title = book.xpath(xpath_title).get()
            price = book.xpath(xpath_price).get()
            is_boolean = True if book.xpath(xpath_is_boolean).get() else False
            print(f"Libro: {title}, Precio: {price}, Disponible: {is_boolean}")
        print(f"Hay {len(books)} libros en la página")
        pass

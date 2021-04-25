import scrapy

class ChartzScraper(scrapy.Spider):
    name = 'snep'
    start_urls = ['https://snepmusique.com/les-certifications']

    def parse(self, response):
        for certifications in response.css('div.certification'):
            yield {
                'artiste': certifications.css('div.artiste::text').get(),
                'titre': certifications.css('div.titre::text').get(),
                'categorie': certifications.css('div.categorie::text').get(),
                'editeur': certifications.css('div.editeur::text').get(),
                'certification': certifications.css('div.certif::text').get(),
            }

#        pour lancer le scraper sur Scrapy:
#        "scrapy runspider chartzscraper.py -O nomfichier.json" (ou .csv)
#
#        /!\ en attente d'une réponse du professeur
#
#        next_page = response.css('div.next').attrib['href']
#        if next_page is not None:
#            yield response.follow(next_page, callback=self.parse)

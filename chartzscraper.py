import scrapy

class ChartzScraper(scrapy.Spider):
    name = 'snep'
    lien = 'https://snepmusique.com/les-certifications/page/'
    for i in range(100):
        lienConcat = lien+str(i)
        start_urls = [lienConcat]

        def parse(self, response):
            for certifications in response.css('div.certification'):
                yield {
                    'artiste': certifications.css('div.artiste::text').get(),
                    'titre': certifications.css('div.titre::text').get(),
                    'categorie': certifications.css('div.categorie::text').get(),
                    'editeur': certifications.css('div.editeur::text').get(),
                    'certification': certifications.css('div.certif::text').get(),
                }

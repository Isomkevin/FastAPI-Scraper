from requests_html import HTMLSession

# https://quotes.toscrape.com/
# https://quotes.toscrape.com/tag/life/

class Scraper():
    def scrapedata(self, tag):
        url = f'https://quotes.toscrape.com/tag/{tag}'
        s = HTMLSession()
        r = s.get(url)
        print(r.status_code)

        qlist = []

        quotes = r.html.find('div.quote')

        for q in quotes:
            q_item = {
                'text': q.find('span.text', first=True).text.strip(),
                'Author': q.find('small.author', first=True).text.strip()

            }
            # print (q_item)
            qlist.append(q_item)
        return qlist    


if __name__ == '__main__':
    quotes = Scraper()
    # Scrape data for 'life' tag
    quotes.scrapedata('life')
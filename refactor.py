import requests
from bs4 import BeautifulSoup

stranka = "https://www.coolinarka.cz/"

class WebPage:
    def __init__(self, url):
        self.url = url
        self.linked_pages_internal = []                 #pages that remain in the same domain
        self.working_pages = []
        self.linked_pages_external = []                  #pages that are outside the domain
        self.linked_pages_objects = []  

    def __repr__(self):
        return self.linked_pages_internal

    def __contains__(self, page):
        return page in self.linked_pages

    # METODY -----------------------------------------
    
    def search_domain(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            pass
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            link_href = link.get('href')

            if link_href == None:                              # checking for <a> without the href argument
                continue
            if link_href[0] == "#":                            # checking for links that link to the same page
                continue

            if link_href[:len(self.url)] == self.url:          # checking for pages with the same domain part (https://page.../) - stay in domain
                self.linked_pages_internal.append(link_href)
            if link_href[0] == "/" and len(link_href) > 1:     # checking for pages that start with "/" - stay in domain
                self.linked_pages_internal.append(str(self.url) + link_href[1:])
            else:
                self.linked_pages_external.append(link_href)

        self.linked_pages_internal = list(dict.fromkeys(self.linked_pages_internal))    # "quick" and dirty - getting rid of duplicates trough dict
        self.linked_pages_external = list(dict.fromkeys(self.linked_pages_external))

        self.sort_code404_pages()



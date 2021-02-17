import requests
from bs4 import BeautifulSoup

stranka = "https://www.coolinarka.cz/"

# Global var

webpage_set = set()
url_set = set()

class WebPage:
    def __init__(self, url):
        self.url = url
        self.linked_pages = []                 #pages that remain in the same domain
        self.working_pages = []
        self.linked_pages_objects = []  

    def __repr__(self):
        return self.url

    # def __contains__(self, page):
    #     return page in self.linked_pages

# FUNCTIONS -----------------------------------------

def sort_working_sites(site_list):
    return_list = []

    for site in site_list:
        response = requests.head(site)
        if response.status_code == 200:
            return_list.append(site)

    return return_list

def site_crawl(url):
    linked_pages = []
    response = requests.get(url)

    # if response.status_code == 200:
    #     pass

    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        link_href = link.get('href')

        if link_href == None:                              # checking for <a> without the href argument
            continue
        if link_href[0] == "#":                            # checking for links that link within the same site
            continue

        if link_href[:len(url)] == url:          # checking for sites with the same domain part (https://site.../...) - stay in domain
            linked_pages.append(link_href)
        if link_href[0] == "/" and len(link_href) > 1:     # checking for site that start with "/" - stay in domain
            linked_pages.append(str(url) + link_href[1:])

    return linked_pages

def create_Webpage_objs(url, working_pages):
    return_list = []

    for site in working_pages:
        site = WebPage(site)
        return_list.append(site)
    return return_list


def search_site(WebPage_obj):
    global url_set
    global webpage_set

    search_url = WebPage_obj.url

    if search_url in url_set:
        return

    linked_pages = site_crawl(search_url)
    if linked_pages == []:
        return
                                                             # TODO: Replace list by set to not allow duplicates
    linked_pages = list(dict.fromkeys(linked_pages))    # "quick" (not really quick) and dirty - getting rid of duplicates trough dict 
    linked_pages_working = sort_working_sites(linked_pages)

    WebPage_obj.working_pages = linked_pages_working

    WebPage_list = create_Webpage_objs(search_url, linked_pages_working)

    print(
        "prošlá webovka: ", WebPage_obj.url, "\n"
        "odkazy: ", linked_pages_working, "\n"
        "-------------------------------------------\n"
    )
    url_set.add(search_url)
    webpage_set.add(WebPage_obj)

    print(
        "url set: ", str(url_set), "\n"
        "webpage set: ", str(webpage_set), "\n"
        "------------------------------------------\n"
    )

    for site in WebPage_list:
        search_site(site)

####################################################################################################
# BOOT SEQUENCE

print("Python website topology program v1. For more info, type help.")

while True:
    user_input = input()

    if user_input == "search":
        url = input("search url?: ")
        url = WebPage(url)
        search_site(url)

        print(
            "\n"
            "#####################################################################################################\n"
            "PROHLEDAVANI DOKONCENO"
        )

        print("testy")
        print("delka webpage_set = ", len(webpage_set))
        print("delka url_set = ", len(url_set))

    if user_input == "test":
        for webpage in webpage_set:
            print("Webpage url: ", webpage.url)
            print("Webpage odkazy: ", webpage.working_pages)
            print("-----------------------------------------------------------------------------------------------------")
            

            #zkouška gitu
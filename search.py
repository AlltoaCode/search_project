import requests
from bs4 import BeautifulSoup

#TEST SITE :)
stranka = "https://www.coolinarka.cz/"

#VARIABLES THAT GET SET IN main.py
verbose = False
max_sites = 50
search_url = ""

# GLOBAL VARS
webpage_set = set()
url_set = set()

#WEBPAGE CLASS
class WebPage:
    def __init__(self, url):
        self.url = url
        self.working_pages = []

    def __repr__(self):
        return self.url

# FUNCTIONS
def sort_working_sites(site_set):
    """ 
    A function that uses the requests library HEAD method to sort working (code 200) pages. Returns list of working sites.
    """

    return_list = []

    for site in site_set:
        response = requests.head(site)
        if response.status_code == 200:
            return_list.append(site)

    return return_list

def site_crawl(url):
    """ 
    A function that uses the requests and BeatufilSoup library to crawl trough a website and return links within the same (second-level) domain.
    """

    linked_pages = set()
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        link_href = link.get('href')

        # checking for <a> without the href argument
        if link_href == None:                              
            continue

        # checking for links that link within the same site
        if link_href[0] == "#":                            
            continue
        
        # checking for sites with the same domain part (https://site.../...) - stay in domain
        if link_href[:len(search_url)] == search_url:          
            linked_pages.add(link_href)

        # checking for site that start with "/" - stay in domain
        if link_href[0] == "/" and len(link_href) > 1:     
            linked_pages.add(str(url) + link_href[1:])

    return linked_pages

def create_Webpage_objs(working_pages):
    """
    A function that takes a list of URLs and returns that list as WebPage objects.
    """

    return_list = []

    for site in working_pages:
        site = WebPage(site)
        return_list.append(site)
    return return_list


def search_site(WebPage_obj):
    """
    A function that takes a WebPage obj, crawls trough it (using site_crawl() ) and than consecutively crawls trough its linked sites until a stop condition is reached. Does not have a return value, saves to global sets.
    """


    global url_set
    global webpage_set

    search_url = WebPage_obj.url

    # checks if the max number of sites visited was not reached
    if max_sites <= len(url_set) and max_sites != 0:
        return

    # checks if this page was already visited
    if search_url in url_set:
        return

    # checks if the page is a dead end
    linked_pages = site_crawl(search_url)
    if linked_pages == {}:
        return

    # Sorting working sites, adding them as a list to the current WebPage obj and creating a list of WebPage objs out of the linked sites
    linked_pages_working = sort_working_sites(linked_pages)
    WebPage_obj.working_pages = linked_pages_working
    WebPage_list = create_Webpage_objs(linked_pages_working)

    if verbose == True:
        print(
            f"visited website: {WebPage_obj.url} \n"
            f"links: {linked_pages_working} \n"
            "\n"
        )
    
    # Adding the current URL/WebPage obj to global sets
    url_set.add(search_url)
    webpage_set.add(WebPage_obj)

    # aaand calling itself
    for site in WebPage_list:
        search_site(site)


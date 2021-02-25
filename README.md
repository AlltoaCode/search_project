
# search_project - Website search

## Quick description:
this program takes an URL as an input and searches trough all the links that lead to some other page within the same second-level domain. Then it displays a simplified graph of the links connecting websites.
  
## How to use:
You control the program by passing it command line arguments.  
The typical use would be:

>$python main.py (--verbose | -n | -o | -m | ...) \<URL\> (<OUTPUT_FILE>) (<MAX_NUMBER_OF_VISITED_SITES>)

you can run `$python main.py -h` or `$python main.py --help` to display the list of availibe options and an explanation of arguments.

### List of options

* -v , --version      - shows version
* -h , --help         - displays the help message
* -o , --output       - optional, output file (WILL REVRITE FILE IF EXISTING) -- NOT FINISHED YET
                      - Use: provide URL first, the second argument will be taken as an output file if -o is used
    , --verbose       - optional, will print to stdout progress reports
* -n , --novisuals    - optional, will not provide visualisation
* -m , --max          - optional, will change max number of visited sites
                      - By defaulst num of visited sites = 50!
                      - Set to 0 to not stop untill all visited, WARNING, might cause problems with extensive sites!
 
### Explaining arguments

* 1st arg             - webpage URL
* 2nd arg             - optional, if -o is used, then output file
* 3rd arg             - optional, if -m is used, then number of visited sites
                    if -m is used and not -o, then 2nd arg will be taken as -m, but -o takes priority!
* More args then needed will be ignored - does not raise an exeption!

>So, one argument is needed at all times, which will be used as the URL. The second one will be the output file (if -o is used), the third will be for selecting the maximum number of sites visited (if -m is used). If only -o or only -m is used, the first argument will still pass the URL and the second will pass the output file  or maximum number of sites visited respectively.

## Dependecies
This program uses requests, BeautifulSoup, networkx and mathplotlib

### TL;DR

Run the program from the command line, choose any options you wish and add at least the webpage URL - more if you choose -o or -m.

---

## Inner workings

- **main.py**

This main file contains the command lige argument parser, and mostly works as a driver code for the rest of the project. 

- **refactor.py** \- better name pending

This file (a refactor of the original search.py) contains all the code for the actual crawling trough the websites.

Notable parts include the `WebPage Class`, which is used for storing data about each individual website visited, as it stores the sites URL and all the links that lead from it to other sites (within the same second level domain)

The two most important functions are the `search_site()` and `site_crawl()`. Site crawl does the actuall connecting to the site, using the requests library for python and then parses it using the BeautifulSoup library. Then it returns a list with all the links from the site. Search site is the funcion that is called recursively, it finds the links that lead to other sites within the same second-level domain from all of the ones returned by site crawl. It also has some control features, for example not to call itself if a site has already been crawled trough.

And last but not least, two global sets should be mentioned, `webpage_set` and `url_set`. While pretty self explanatory, they are a very important part of refactor.py. Webpage set stores all the sites as a WebPage object and is later used to draw the graph. Url set stores the urls of the sites visited, so that checking if site has been visited or not. While this may seem like storing two of the same things, url set only stores the urls as strings, so checking if url is in url_set works nicely, while even if two WebPage objects have the exact same data, they are not the same object and checking using them would be way harder.

- **visualize.py**:

The shortets of the three files works to draw the websites with together with their links as a graph in mathplotlib. It does this with a combination of networkx and mathplotlib, taking the webpage_set from refactor.py
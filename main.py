import requests
import refactor
import visualize
import sys

# MESSAGES
VERSION = "version 1.0"
HELP = """ Program for visualizing website topology     

        Usage: main.py (--verbose | -n | -o | -m | ...) <URL> (<OUTPUT_FILE>) (<MAX_NUMBER_OF_VISITED_SITES>)"

        Options:    -v , --version      shows version
                    -h , --help         this help message
                    -o , --output       optional, output file (WILL REVRITE FILE IF EXISTING)
                                        Use: provide URL first, the second argument will be taken as an output file if -o is used
                       , --verbose      optional, will print to stdout progress reports
                    -n , --novisuals    optional, will not provide visualisation
                    -m , --max          optional, will change max number of visited sites
                                        By defaulst num of visited sites = 50!
                                        Set to 0 to not stop untill all visited, WARNING, might cause problems with extensive sites!

        Arguments:  1st arg             webpage URL
                    2nd arg             optional, if -o is used, then output file
                    3rd arg             optional, if -m is used, then number of visited sites
                                        if -m is used and not -o, then 2nd arg will be taken as -m, but -o takes priority!
                    More args then needed will be ignored - does not raise an exeption!
        """

# CONSTS
opts_list = ["-v","--version","-h","--help","-o","--output","--verbose","-n","--novisuals","-m","--max"]


# SETTINGS BOOLS
verbose = False      #done
novisuals = False    #done
output = False
max_override = False

# MAX NUMBER OF SITES VISITED
max_num_sites = 50

# PARSING
options = [opt for opt in sys.argv[1:] if opt.startswith("-")]
arguments = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if "-v" in options or "--version" in options:
    print(VERSION)
    raise SystemExit()
if "-h" in options or "--help" in options:
    print(HELP)
    raise SystemExit()

if "--verbose" in options:
    verbose = True
if "-n" in options or "--novisuals" in options:
    novisuals = True
if "-o" in options or "--output" in options:
    output = True
if "-m" in options or "--max" in options:
    max_override = True


# HANDLING UKNOWN OPTS
for opt in options:
    if opt not in opts_list:
        raise SystemExit(f"Uknown option {opt}! Usage: {sys.argv[0]} (--verbose | -n | -o | -m | ...) <URL> (<OUTPUT_FILE>) (<MAX_NUMBER_OF_VISITED_SITES>)")

# HANDLING NO ARGS (OR LESS THAN EXPECTED) - (any extra arg gets ignored)
if (output == False and max_override == False) and len(arguments) < 1:
    raise SystemExit(f"Insufficient number of arguments {len(arguments)}, expected 1! Usage: {sys.argv[0]} (--verbose | -n | -o | -m | ...) <URL> (<OUTPUT_FILE>) (<MAX_NUMBER_OF_VISITED_SITES>)")
if (output == True and max_override == True) and len(arguments) < 3:
    raise SystemExit(f"Insufficient number of arguments {len(arguments)}, expected 3! Usage: {sys.argv[0]} (--verbose | -n | -o | -m | ...) <URL> (<OUTPUT_FILE>) (<MAX_NUMBER_OF_VISITED_SITES>)") 
if (output == True and len(arguments) < 2) or (max_override == True and len(arguments) < 2) :
    raise SystemExit(f"Insufficient number of arguments {len(arguments)}, expected 2! Usage: {sys.argv[0]} (--verbose | -n | -o | -m | ...) <URL> (<OUTPUT_FILE>) (<MAX_NUMBER_OF_VISITED_SITES>)") 

# CHECKING THAT URL IS VALID
try:
    requests.head(arguments[0])
except:
    raise SystemExit(f"Cannot connect to URL! Is this URL: {arguments[0]} valid?") 

# DRIVER CODE 
url = arguments[0]
if verbose == True:
    print(f"url is: {url}")

if output == True and max_override == False:
    output_file = arguments[1]
    if verbose == True:
        print(f"out file is: {output_file}")

if output == False and max_override == True:
    max_num_sites = int(arguments[1])
    if verbose == True:
        print(f"max num of sites is: {max_num_sites}")

if output == True and max_override == True:
    output_file = arguments[1]
    max_num_sites = int(arguments[2])
    if verbose == True:
        print(f"out file is: {output_file}")
        print(f"max num of sites is: {max_num_sites}")

if verbose == True:
    print("\n")

# DRIVER CODE - RUNNING THE SEARCH FROM THE REFACTOR FILE

refactor.ref_verbose = verbose          # setting verbose in the refactor file
refactor.ref_max_sites = max_num_sites
url = refactor.WebPage(url)
refactor.search_site(url)


# DRIVER CORE - DRAWING A GRAPH


if novisuals == False:
    visualize.draw_graph(refactor.webpage_set)
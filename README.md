
# search_project - Website search

## Quick description:
this program takes an URL as an input and searches trough all the links that link to some other page within the same second-level domain. Then it displays a simplified graph of the links connecting websites.
  
## How to use:
You control the program by passing it command line arguments.  
The typical use would be:

$python main.py (--verbose | -n | -o | -m | ...) <URL> (<OUTPUT_FILE>) (<MAX_NUMBER_OF_VISITED_SITES>)

you can run $python main.py -h or --help to display the list of availibe options and an explanation of arguments.

### List of options

-v , --version      shows version
-h , --help         displays the help message
-o , --output       optional, output file (WILL REVRITE FILE IF EXISTING) -- NOT FINISHED YET
                    Use: provide URL first, the second argument will be taken as an output file if -o is used
    , --verbose     optional, will print to stdout progress reports
-n , --novisuals    optional, will not provide visualisation
-m , --max          optional, will change max number of visited sites
                    By defaulst num of visited sites = 50!
                    Set to 0 to not stop untill all visited, WARNING, might cause problems with extensive sites!

### Explaining arguments

1st arg             webpage URL
2nd arg             optional, if -o is used, then output file
3rd arg             optional, if -m is used, then number of visited sites
                    if -m is used and not -o, then 2nd arg will be taken as -m, but -o takes priority!
More args then needed will be ignored - does not raise an exeption!

So, one argument is needed at all times, which will be used as the URL. The second one will be the output file (if -o is used), the third will be for selecting the maximum number of sites visited (if -m is used). If only -o or only -m is used, the first argument will still pass the URL and the second will pass the output file or maximum number of sites visited respectively.
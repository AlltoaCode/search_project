import networkx as nx 
import matplotlib.pyplot as plt 
   
# GRAPH CLASS
class GraphSimplify: 
    """
    used to simplify the way of adding edges to the networkx graph, first saving them internally, then passing them all at once with the call of visualize().
    """

    def __init__(self): 
        self.edges = [] 
          
    def addEdge(self, a, b): 
        temp = [a, b] 
        self.edges.append(temp) 

    def visualize(self): 
        G = nx.MultiGraph() 
        G.add_edges_from(self.edges) 
        nx.draw_networkx(G) 
        plt.show() 
  
# FUNCTIONS
def draw_graph(set_of_WebPage_objs):
    """
    Function used for drawing the Graph itself, takes a set of WebPage objects, adds egdes between each object URL and linked URLs, then calls visualize() to draw the graph.
    """

    G = GraphSimplify() 

    for webpage in set_of_WebPage_objs:
        for linked_page in webpage.working_pages:
            G.addEdge(webpage.url,linked_page)

    G.visualize() 


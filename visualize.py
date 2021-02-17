import networkx as nx 
import matplotlib.pyplot as plt 
   
  
class GraphVisualization: 
   
    def __init__(self): 
        self.visual = [] 
          
    def addEdge(self, a, b): 
        temp = [a, b] 
        self.visual.append(temp) 

    def visualize(self): 
        G = nx.Graph() 
        G.add_edges_from(self.visual) 
        nx.draw_networkx(G) 
        plt.show() 
  

def draw_graph(list_of_WebPage_objs):
    G = GraphVisualization() 

    for webpage in list_of_WebPage_objs:
        for linked_page in webpage.working_pages:
            G.addEdge(webpage.url,linked_page)

    G.visualize() 


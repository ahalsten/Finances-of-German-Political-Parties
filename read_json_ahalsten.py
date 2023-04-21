#################################
# SI507: Final Project
# Winter 2023
# Anna Halstenbach
# uniqname: ahalsten
# Import Graph from json
#################################

import networkx as nx
import json

def read_json_file(filename):
    '''Reads a json file and returns graph from node-link data format.

    Parameters:
        filename (str): name of json file

    Returns:
        MultiDiGraph: deserialized graph
    '''
    with open(filename, 'r') as f:
        js_graph = json.loads(json.load(f))
    return nx.node_link_graph(js_graph, directed=True)

G = read_json_file('mydata.json')
# print(G)
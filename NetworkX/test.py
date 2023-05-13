from operator import itemgetter

from networkx import flow_hierarchy, nodes, number_of_nodes, all_neighbors
from networkx.algorithms import community  # PACKAGE FOR COMMUNITY DETECTION NEEDS TO BE IMPORTED SEPARATELY
import networkx as nx
import matplotlib.pyplot as plt
import xlrd
import itertools
import mpld3
import pandas as pd


# THE FOLLOWING BLOCK OF CODE IMPORTS THE EXCEL DATASET, SORTS THE FILE BY SHEET, EXTRACTS THE DATA
# AND SLICES THE DATA INTO ITS RESPECTIVE PLACEHOLDERS
# NODE 1 STORES THE SENDING AS, NODE 2 STORES THE RECEIVING AS, REL1 STORES THE AS RELATIONSHIP

# file1998 = "C:/Users/marya/Desktop/DISSERTATION/dataset/19980101.as-rel.xls"

G1998 = nx.DiGraph()
P = nx.DiGraph()
domains1998 = []
total_domains = []
path = []

# book1998 = xlrd.open_workbook(file1998)
# sheet1998 = book1998.sheet_by_index(0)

# for row in range(sheet1998.nrows):
#     data = sheet1998.row_slice(row)
#     node1 = str(int(data[0].value))
#     node2 = str(int(data[1].value))
#     rel1 = str(int(data[2].value))
#     G1998.add_edge(node1, node2, rel=rel1)
#     domains1998.append((node1, node2))
#     total_domains.append(node1)
#     total_domains.append(node2)

# G1998.add_edges_from(domains1998)  # THE EDGES IN THE DATASET ARE ADDED TO THE DIRECTED GRAPH, G
# print(G1998.number_of_nodes())

file19 = "C:/Users/marya/Desktop/DISSERTATION/dataset/F1998.xlsx"

G2009 = nx.DiGraph()
g = nx.DiGraph()
P = nx.Graph()
domains2009 = []
total_domains = []
in_path = []
out_path = []

# book2009 = xlrd.open_workbook(file2009)
# sheet2009 = book2009.sheets()
#
# for row in range(sheet2009.nrows):
#     data = data.row_slice(row)
#     node1 = str(int(data[0].value))
#     node2 = str(int(data[1].value))
#     rel1 = str(int(data[2].value))
#     G2009.add_edge(node1, node2, rel=rel1)
#     domains2009.append((node1, node2))
#     total_domains.append(node1)
#     total_domains.append(node2)

# G2009.add_edges_from(domains2009)  # THE EDGES IN THE DATASET ARE ADDED TO THE DIRECTED GRAPH, G

df = pd.read_excel(file19)
G = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship', create_using=nx.Graph())

print(G.number_of_nodes())
# path = [(nx.shortest_simple_paths(G, 33, 1))]
# # path = [tuple(val) for dic in path for key, val in dic.items()]
# # path = path[1:]
# for node_tuple in path:
#     P.add_edges_from(itertools.combinations(node_tuple, 2))

# for node1, node2, data in P.edges(data=True):
#     print(data["relationship"])
# nx.draw(G, with_labels=True)

# INTERNET HIERARCHY IMPLEMENTATION: USING IF STATEMENT AND EDGE_ATTR
TIER_3 = "NO CUSTOMERS I.E IS NOT A PROVIDER TO ANOTHER AS, " \
         "DOES NOT HAVE A -1 RELATIONSHIP WITH ANOTHER AS BUT CAN HAVE PEERS" \
        "IF IN-DEGREE==0"
TIER_2 = "HAS A PROVIDER AND CUSTOMER, IF IN-DEGREE AND OUT-DEGREE >1"
TIER_1 = "NO PROVIDERS I.E IS NOT A CUSTOMER TO ANOTHER AS BUT CAN HAVE PEERS" \
        "IF OUT-DEGREE==0"

# THE FOLLOWING BLOCK OF CODE DIFFERENTIATES THE COLOR OF THE EDGES BY THEIR RELATIONSHIP
# PROVIDER-CUSTOMER RELATIONSHIP IS TAGGED RED, PEER RELATIONSHIP IS TAGGED BLUE
color_map = nx.get_edge_attributes(G, "relationship")

for key in color_map:
    if color_map[key] == 0:
        color_map[key] = "blue"
    elif color_map[key] == -1:
        color_map[key] = "red"

rel_colors = [color_map.get(edge) for edge in G.edges()]
# node_sizes = [(total_domains.count(node)*100) for node in G.nodes()]

# pos = nx.planar_layout(P)
# nx.draw(P, with_labels=True, edge_color=rel_colors)
# plt.show()
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, edge_color=rel_colors)
# plt.show()

# THE FOLLOWING BLOCK OF CODE CALCULATES THE LOGICAL SHORTEST PATH OF A NODE TO ITS DESTINATION

# print(nx.has_path(G, 1, 114))
# if nx.has_path(G, 1, 114):
#     print(nx.shortest_path(G, 1, 114))
# else:
#     print("No Path")
# domain = str(17)

# out_path.append(nx.single_source_shortest_path(G, 33, 1))
# out_path = [tuple(val) for dic in out_path for key, val in dic.items()]
# out_path = out_path[1:]

in_path.append(nx.single_source_shortest_path(G, 1, 1))
in_path = [tuple(val) for dic in in_path for key, val in dic.items()]
in_path = in_path[1:]

# print(in_path)
# print(out_path)
# for node_tuple in out_path:
#     P.add_edges_from(itertools.combinations(node_tuple, 2))

for node_tuple in in_path:
    P.add_edges_from(itertools.combinations(node_tuple, 2))

pos = nx.spring_layout(P)
fig = nx.draw(P, pos, with_labels=True, edge_color=rel_colors)

# THE FOLLOWING BLOCK OF CODE CALCULATES THE CENTRALITY MEASURES OF THE NODES IN THE NETWORK AND THE NETWORK AS A WHOLE

# eigen vector centrality - how important a node is based on the value of its link nodes
# betweenness centrality - how much percent of the optimal paths pass through a node,
# how often do other nodes need to pass through a particular node
# density - percentage of nodes which are interconnected
# domain = "3"
# degree = dict(G.degree)
# in_degree = dict(G.in_degree)
# out_degree = dict(G.out_degree)
# btw_c = nx.betweenness_centrality(G)
# eigen_c = nx.eigenvector_centrality(G)
# nx.set_node_attributes(G, degree, 'Degree')
# nx.set_node_attributes(G, in_degree, 'In-degree')
# nx.set_node_attributes(G, out_degree, 'Out-degree')
# nx.set_node_attributes(G, btw_c, 'Betweenness')
# nx.set_node_attributes(G, eigen_c, 'Eigenvector')
# attributes = dict(G.nodes[domain])
#
# sorted_degree = sorted(eigen_c.items(), key=itemgetter(1), reverse=True)
# print("Top 20 nodes by eigenvalue:")
# for d in sorted_degree[:20]:
# print(d)

# THE FOLLOWING BLOCK OF CODE CALCULATES THE COMMUNITIES IN THE NETWORK, IDENTIFIES THE SUBCLASSES
# MODULARITY IS A MEASURE OF RELATIVE DENSITY USED TO CALCULATE THE COMMUNITY METRIC,
# A COMMUNITY HAS HIGHER DENSITY WITH NODES WITHIN ITS CLASS
# AND LOWER DENSITY WITH NODES OUTSIDE ITS CLASS, SIDE NOTE: IT IS NOT FULLY CONNECTED TO NODES OUTSIDE ITS CLASS
# communities = community.greedy_modularity_communities(G)
# modularity_dict = {}
# for i, c in enumerate(communities):
#     for node in c:
#         modularity_dict[node] = i
#
# nx.set_node_attributes(G, modularity_dict, 'Modularity Class')

# print(G.number_of_nodes())  # COUNTS THE NUMBER OF NODES IN THE GRAPH
# print(G.nodes())  # LISTS THE NODES IN THE GRAPH
# print(list(all_neighbors(G, "33"))) # LISTS THE NEIGHBOURING NODES TO NODE 33

# for i, c in enumerate(communities):  # LISTS THE MODULARITY CLASSES AND ITS MEMBERS
# if len(c) > 2:
# print('Class '+str(i)+':', list(c))


# THE FOLLOWING BLOCK OF CODE PRODUCES THE GRAPH OF THE NETWORK
# SPRING_LAYOUT IS A GRAPH STYLE, EDGE_COLOR DICTATES THE COLOR OF THE EDGE DEPENDING ON ITS RELATIONSHIP,
# NODE_SIZE VARIES THE SIZE OF THE NODE TO DEPEND ON ITS NUMBER OF EDGES

# pos = nx.spring_layout(G1998)

# nx.draw(G1998, pos, with_labels=True, edge_color=rel_colors)
# nx.draw(P, with_labels=True, edge_color=rel_colors)
# plt.show()
# plt.savefig("graph1998.png")

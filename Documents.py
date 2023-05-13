import networkx as nx
from networkx import number_of_nodes, dorogovtsev_goltsev_mendes_graph, number_of_edges
import pandas as pd
import matplotlib.pyplot as plt


def file_upload(file):
    G = nx.DiGraph()
    domains = []
    total_domains = []

    book = xlrd.open_workbook(file)
    sheet = book.sheet_by_index(0)

    for row in range(sheet.nrows):
        data = sheet.row_slice(row)
        node1 = str(int(data[0].value))
        node2 = str(int(data[1].value))
        rel1 = str(int(data[2].value))
        G.add_edge(node1, node2, rel=rel1)
        domains.append((node1, node2))
        total_domains.append(node1)
        total_domains.append(node2)

    G.add_edges_from(domains)  # THE EDGES IN THE DATASET ARE ADDED TO THE DIRECTED GRAPH, G
    return G


# THIS FUNCTION IS CREATED TO GET THE INDEX OF THE DATE IN A LIST G
def get_index_of_date(G, date):
    if type(G) == list and date in G:
        index = G.index(date)
        return index
    return f"{date}"


def get_index_of_file(F, date):
    if type(F) == list and date in F:
        file_index = F.index(date)
        return file_index
    return f"{date}"


G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
     2017, 2018, 2019, 2020, 2021, 2022]

## THE DATA IS EXTRACTED FROM THE PANDAS DATAFRAME AND PASSED INTO THE UNDIRECTED GRAPH
# G[0] = nx.Graph()  # creates an undirected graph
# df = pd.read_excel(f"Files/F1998.xlsx")  # pandas is used to extract the data from the file
# G[0] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# COMPUTES THE NETWORK SIZE, NUMBER OF LINKS, NUMBER OF PROVIDER AND PEER LINKS, AND THE DENSITY PROPERTY OF THE GRAPH
# count_1998 = number_of_nodes(G[0])
# print(f"1998: {count_1998}")
# edges_1998 = number_of_edges(G[0])
# print(f"1998_edges: {edges_1998}")
# rel_count_1998 = nx.get_edge_attributes(G[0], "relationship")
# peer_1998 = 0
# provider_1998 = 0
# for key in rel_count_1998:
#     if rel_count_1998[key] == 0:
#         peer_1998 += 1
#     elif rel_count_1998[key] == -1:
#         provider_1998 += 1
#
# print(f"peer_1998: {peer_1998}")
# print(f"provider_1998: {provider_1998}")
#
# density_1998 = nx.density(G[0])
# print(f"density_1998: {density_1998}")
#
# EDGE COLORS ARE ASSIGNED DEPENDING ON THE RELATIONSHIP ATTRIBUTE VALUE
# color_map_1998 = nx.get_edge_attributes(G[0], "relationship")
#
# for key in color_map_1998:
#     if color_map_1998[key] == 0:
#         color_map_1998[key] = "blue"
#     elif color_map_1998[key] == -1:
#         color_map_1998[key] = "red"
#
# rel_colors_1998 = [color_map_1998.get(edge) for edge in G[0].edges()]
# degree = dict(G[0].degree)
# nx.set_node_attributes(G[0], degree, "Degree")
# value = nx.get_node_attributes(G[0], "Degree")
# H= nx.Graph()
# for node1, node2 in G[0].edges():
#     if value[node2] > 130:
#         H.add_edge(node1, node2)

# THE GRAPH P IS GENERATED WITH A SPRING LAYOUT
# PLT.CLOSE() PREVENTS THE GRAPHS FROM GENERATING A LEYERED PLOT ON THE PREVIOUSLY GENERATED PLOT
# pos_1998 = nx.spring_layout(H)
# nx.draw(H, pos_1998, with_labels=True, edge_color=rel_colors_1998)
# plt.plot(figsize=(20, 15))
# plt.savefig("static/G1998.png")
# plt.close()


# G[1] = nx.Graph()
# df = pd.read_excel(f"Files/F1999.xlsx")
# G[1] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_1999 = number_of_nodes(G[1])
# print(f"1999: {count_1999}")
# edges_1999 = number_of_edges(G[1])
# print(f"1999_edges: {edges_1999}")
# rel_count_1999 = nx.get_edge_attributes(G[1], "relationship")
# peer_1999 = 0
# provider_1999 = 0
# for key in rel_count_1999:
#     if rel_count_1999[key] == 0:
#         peer_1999 += 1
#     elif rel_count_1999[key] == -1:
#         provider_1999 += 1
#
# print(f"peer_1999: {peer_1999}")
# print(f"provider_1999: {provider_1999}")
#
# density_1999 = nx.density(G[1])
# print(f"density_1999: {density_1999}")

# color_map_1999 = nx.get_edge_attributes(G[1], "relationship")
#
# for key in color_map_1999:
#     if color_map_1999[key] == 0:
#         color_map_1999[key] = "blue"
#     elif color_map_1999[key] == -1:
#         color_map_1999[key] = "red"
#
# rel_colors_1999 = [color_map_1999.get(edge) for edge in G[1].edges()]
# pos_1999 = nx.spectral_layout(G[1])
# nx.draw(G[1], pos_1999, with_labels=True, edge_color=rel_colors_1999)
# plt.savefig("static/graph/G1999.png")
# plt.close()


# G[2] = nx.Graph()
# df = pd.read_excel(f"Files/F2000.xlsx")
# G[2] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2000 = number_of_nodes(G[2])
# print(f"2000: {count_2000}")
# edges_2000 = number_of_edges(G[2])
# print(f"2000_edges: {edges_2000}")
# rel_count_2000 = nx.get_edge_attributes(G[2], "relationship")
# peer_2000 = 0
# provider_2000 = 0
# for key in rel_count_2000:
#     if rel_count_2000[key] == 0:
#         peer_2000 += 1
#     elif rel_count_2000[key] == -1:
#         provider_2000 += 1
#
# print(f"peer_2000: {peer_2000}")
# print(f"provider_2000: {provider_2000}")
#
# density_2000 = nx.density(G[2])
# print(f"density_2000: {density_2000}")

# color_map_2000 = nx.get_edge_attributes(G[2], "relationship")
#
# for key in color_map_2000:
#     if color_map_2000[key] == 0:
#         color_map_2000[key] = "blue"
#     elif color_map_2000[key] == -1:
#         color_map_2000[key] = "red"
#
# rel_colors_2000 = [color_map_2000.get(edge) for edge in G[2].edges()]
# pos_2000 = nx.spectral_layout(G[2])
# nx.draw(G[2], pos_2000, with_labels=True, edge_color=rel_colors_2000)
# plt.savefig("static/graph/G2000.png")
# plt.close()


# G[3] = nx.Graph()
# df = pd.read_excel(f"Files/F2001.xlsx")
# G[3] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2001 = number_of_nodes(G[3])
# print(f"2001: {count_2001}")
# edges_2001 = number_of_edges(G[3])
# print(f"2001_edges: {edges_2001}")
# rel_count_2001 = nx.get_edge_attributes(G[3], "relationship")
# peer_2001 = 0
# provider_2001 = 0
# for key in rel_count_2001:
#     if rel_count_2001[key] == 0:
#         peer_2001 += 1
#     elif rel_count_2001[key] == -1:
#         provider_2001 += 1
#
# print(f"peer_2001: {peer_2001}")
# print(f"provider_2001: {provider_2001}")
#
# density_2001 = nx.density(G[3])
# print(f"density_2001: {density_2001}")

# color_map_2001 = nx.get_edge_attributes(G[3], "relationship")
#
# for key in color_map_2001:
#     if color_map_2001[key] == 0:
#         color_map_2001[key] = "blue"
#     elif color_map_2001[key] == -1:
#         color_map_2001[key] = "red"
#
# rel_colors_2001 = [color_map_2001.get(edge) for edge in G[3].edges()]
# pos_2001 = nx.spectral_layout(G[3])
# nx.draw(G[3], pos_2001, with_labels=True, edge_color=rel_colors_2001)
# plt.savefig("static/graph/G2001.png")
# plt.close()


# G[4] = nx.Graph()
# df = pd.read_excel(f"Files/F2002.xlsx")
# G[4] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2002 = number_of_nodes(G[4])
# print(f"2002: {count_2002}")
# edges_2002 = number_of_edges(G[4])
# print(f"2002_edges: {edges_2002}")
# rel_count_2002 = nx.get_edge_attributes(G[4], "relationship")
# peer_2002 = 0
# provider_2002 = 0
# for key in rel_count_2002:
#     if rel_count_2002[key] == 0:
#         peer_2002 += 1
#     elif rel_count_2002[key] == -1:
#         provider_2002 += 1
#
# print(f"peer_2002: {peer_2002}")
# print(f"provider_2002: {provider_2002}")
#
# density_2002 = nx.density(G[4])
# print(f"density_2002: {density_2002}")

# color_map_2002 = nx.get_edge_attributes(G[4], "relationship")
#
# for key in color_map_2002:
#     if color_map_2002[key] == 0:
#         color_map_2002[key] = "blue"
#     elif color_map_2002[key] == -1:
#         color_map_2002[key] = "red"
#
# rel_colors_2002 = [color_map_2002.get(edge) for edge in G[4].edges()]
# pos_2002 = nx.spectral_layout(G[4])
# nx.draw(G[4], pos_2002, with_labels=True, edge_color=rel_colors_2002)
# plt.savefig("static/graph/G2002.png")
# plt.close()


# G[5] = nx.Graph()
# df = pd.read_excel(f"Files/F2003.xlsx")
# G[5] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2003 = number_of_nodes(G[5])
# print(f"2003: {count_2003}")
# edges_2003 = number_of_edges(G[5])
# print(f"2003_edges: {edges_2003}")
# rel_count_2003 = nx.get_edge_attributes(G[5], "relationship")
# peer_2003 = 0
# provider_2003 = 0
# for key in rel_count_2003:
#     if rel_count_2003[key] == 0:
#         peer_2003 += 1
#     elif rel_count_2003[key] == -1:
#         provider_2003 += 1
#
# print(f"peer_2003: {peer_2003}")
# print(f"provider_2003: {provider_2003}")
#
# density_2003 = nx.density(G[5])
# print(f"density_2003: {density_2003}")

# color_map_2003 = nx.get_edge_attributes(G[5], "relationship")
#
# for key in color_map_2003:
#     if color_map_2003[key] == 0:
#         color_map_2003[key] = "blue"
#     elif color_map_2003[key] == -1:
#         color_map_2003[key] = "red"
#
# rel_colors_2003 = [color_map_2003.get(edge) for edge in G[5].edges()]
# pos_2003 = nx.spectral_layout(G[5])
# nx.draw(G[5], pos_2003, with_labels=True, edge_color=rel_colors_2003)
# plt.savefig("static/graph/G2003.png")
# plt.close()


# G[6] = nx.Graph()
# df = pd.read_excel(f"Files/F2004.xlsx")
# G[6] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2004 = number_of_nodes(G[6])
# print(f"2004: {count_2004}")
# edges_2004 = number_of_edges(G[6])
# print(f"2004_edges: {edges_2004}")
# rel_count_2004 = nx.get_edge_attributes(G[6], "relationship")
# peer_2004 = 0
# provider_2004 = 0
# for key in rel_count_2004:
#     if rel_count_2004[key] == 0:
#         peer_2004 += 1
#     elif rel_count_2004[key] == -1:
#         provider_2004 += 1
#
# print(f"peer_2004: {peer_2004}")
# print(f"provider_2004: {provider_2004}")
#
# density_2004 = nx.density(G[6])
# print(f"density_2004: {density_2004}")

# color_map_2004 = nx.get_edge_attributes(G[6], "relationship")
#
# for key in color_map_2004:
#     if color_map_2004[key] == 0:
#         color_map_2004[key] = "blue"
#     elif color_map_2004[key] == -1:
#         color_map_2004[key] = "red"
#
# rel_colors_2004 = [color_map_2004.get(edge) for edge in G[6].edges()]
# pos_2004 = nx.spectral_layout(G[6])
# nx.draw(G[6], pos_2004, with_labels=True, edge_color=rel_colors_2004)
# plt.savefig("static/graph/G2004.png")
# plt.close()


# G[7] = nx.Graph()
# df = pd.read_excel(f"Files/F2005.xlsx")
# G[7] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2005 = number_of_nodes(G[7])
# print(f"2005: {count_2005}")
# edges_2005 = number_of_edges(G[7])
# print(f"2005_edges: {edges_2005}")
# rel_count_2005 = nx.get_edge_attributes(G[7], "relationship")
# peer_2005 = 0
# provider_2005 = 0
# for key in rel_count_2005:
#     if rel_count_2005[key] == 0:
#         peer_2005 += 1
#     elif rel_count_2005[key] == -1:
#         provider_2005 += 1
#
# print(f"peer_2005: {peer_2005}")
# print(f"provider_2005: {provider_2005}")
#
# density_2005 = nx.density(G[7])
# print(f"density_2005: {density_2005}")

# color_map_2005 = nx.get_edge_attributes(G[7], "relationship")
#
# for key in color_map_2005:
#     if color_map_2005[key] == 0:
#         color_map_2005[key] = "blue"
#     elif color_map_2005[key] == -1:
#         color_map_2005[key] = "red"
#
# rel_colors_2005 = [color_map_2005.get(edge) for edge in G[7].edges()]
# pos_2005 = nx.spectral_layout(G[7])
# nx.draw(G[7], pos_2005, with_labels=True, edge_color=rel_colors_2005)
# plt.savefig("static/graph/G2005.png")
# plt.close()


# G[8] = nx.Graph()
# df = pd.read_excel(f"Files/F2006.xlsx")
# G[8] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2006 = number_of_nodes(G[8])
# print(f"2006: {count_2006}")
# edges_2006 = number_of_edges(G[8])
# print(f"2006_edges: {edges_2006}")
# rel_count_2006 = nx.get_edge_attributes(G[8], "relationship")
# peer_2006 = 0
# provider_2006 = 0
# for key in rel_count_2006:
#     if rel_count_2006[key] == 0:
#         peer_2006 += 1
#     elif rel_count_2006[key] == -1:
#         provider_2006 += 1
#
# print(f"peer_2006: {peer_2006}")
# print(f"provider_2006: {provider_2006}")
#
# density_2006 = nx.density(G[8])
# print(f"density_2006: {density_2006}")

# color_map_2006 = nx.get_edge_attributes(G[8], "relationship")
#
# for key in color_map_2006:
#     if color_map_2006[key] == 0:
#         color_map_2006[key] = "blue"
#     elif color_map_2006[key] == -1:
#         color_map_2006[key] = "red"
#
# rel_colors_2006 = [color_map_2006.get(edge) for edge in G[8].edges()]
# pos_2006 = nx.spectral_layout(G[8])
# nx.draw(G[8], pos_2006, with_labels=True, edge_color=rel_colors_2006)
# plt.savefig("static/graph/G2006.png")
# plt.close()


# G[9] = nx.Graph()
# df = pd.read_excel(f"Files/F2007.xlsx")
# G[9] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2007 = number_of_nodes(G[9])
# print(f"2007: {count_2007}")
# edges_2007 = number_of_edges(G[9])
# print(f"2007_edges: {edges_2007}")
# rel_count_2007 = nx.get_edge_attributes(G[9], "relationship")
# peer_2007 = 0
# provider_2007 = 0
# for key in rel_count_2007:
#     if rel_count_2007[key] == 0:
#         peer_2007 += 1
#     elif rel_count_2007[key] == -1:
#         provider_2007 += 1
#
# print(f"peer_2007: {peer_2007}")
# print(f"provider_2007: {provider_2007}")
#
# density_2007 = nx.density(G[9])
# print(f"density_2007: {density_2007}")

# color_map_2007 = nx.get_edge_attributes(G[9], "relationship")
#
# for key in color_map_2007:
#     if color_map_2007[key] == 0:
#         color_map_2007[key] = "blue"
#     elif color_map_2007[key] == -1:
#         color_map_2007[key] = "red"
#
# rel_colors_2007 = [color_map_2007.get(edge) for edge in G[9].edges()]
# pos_2007 = nx.spectral_layout(G[9])
# nx.draw(G[9], pos_2007, with_labels=True, edge_color=rel_colors_2007)
# plt.savefig("static/graph/G2007.png")
# plt.close()


# G[10] = nx.Graph()
# df = pd.read_excel(f"Files/F2008.xlsx")
# G[10] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2008 = number_of_nodes(G[10])
# print(f"2008: {count_2008}")
# edges_2008 = number_of_edges(G[10])
# print(f"2008_edges: {edges_2008}")
# rel_count_2008 = nx.get_edge_attributes(G[10], "relationship")
# peer_2008 = 0
# provider_2008 = 0
# for key in rel_count_2008:
#     if rel_count_2008[key] == 0:
#         peer_2008 += 1
#     elif rel_count_2008[key] == -1:
#         provider_2008 += 1
#
# print(f"peer_2008: {peer_2008}")
# print(f"provider_2008: {provider_2008}")
#
# density_2008 = nx.density(G[10])
# print(f"density_2008: {density_2008}")

# color_map_2008 = nx.get_edge_attributes(G[10], "relationship")
#
# for key in color_map_2008:
#     if color_map_2008[key] == 0:
#         color_map_2008[key] = "blue"
#     elif color_map_2008[key] == -1:
#         color_map_2008[key] = "red"
#
# rel_colors_2008 = [color_map_2008.get(edge) for edge in G[10].edges()]
# pos_2008 = nx.spectral_layout(G[10])
# nx.draw(G[10], pos_2008, with_labels=True, edge_color=rel_colors_2008)
# plt.savefig("static/graph/G2008.png")
# plt.close()


# G[11] = nx.Graph()
# df = pd.read_excel(f"Files/F2009.xlsx")
# G[11] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2009 = number_of_nodes(G[11])
# print(f"2009: {count_2009}")
# edges_2009 = number_of_edges(G[11])
# print(f"2009_edges: {edges_2009}")
# rel_count_2009 = nx.get_edge_attributes(G[11], "relationship")
# peer_2009 = 0
# provider_2009 = 0
# for key in rel_count_2009:
#     if rel_count_2009[key] == 0:
#         peer_2009 += 1
#     elif rel_count_2009[key] == -1:
#         provider_2009 += 1
#
# print(f"peer_2009: {peer_2009}")
# print(f"provider_2009: {provider_2009}")
#
# density_2009 = nx.density(G[11])
# print(f"density_2009: {density_2009}")

# color_map_2009 = nx.get_edge_attributes(G[11], "relationship")
#
# for key in color_map_2009:
#     if color_map_2009[key] == 0:
#         color_map_2009[key] = "blue"
#     elif color_map_2009[key] == -1:
#         color_map_2009[key] = "red"
#
# rel_colors_2009 = [color_map_2009.get(edge) for edge in G[11].edges()]
# pos_2009 = nx.spectral_layout(G[11])
# nx.draw(G[11], pos_2009, with_labels=True, edge_color=rel_colors_2009)
# plt.savefig("static/graph/G2009.png")
# plt.close()


# G[12] = nx.Graph()
# df = pd.read_excel(f"Files/F2010.xlsx")
# G[12] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2010 = number_of_nodes(G[12])
# print(f"2010: {count_2010}")
# edges_2010 = number_of_edges(G[12])
# print(f"2010_edges: {edges_2010}")
# rel_count_2010 = nx.get_edge_attributes(G[12], "relationship")
# peer_2010 = 0
# provider_2010 = 0
# for key in rel_count_2010:
#     if rel_count_2010[key] == 0:
#         peer_2010 += 1
#     elif rel_count_2010[key] == -1:
#         provider_2010 += 1
#
# print(f"peer_2010: {peer_2010}")
# print(f"provider_2010: {provider_2010}")
#
# density_2010 = nx.density(G[12])
# print(f"density_2010: {density_2010}")

# color_map_2010 = nx.get_edge_attributes(G[12], "relationship")
#
# for key in color_map_2010:
#     if color_map_2010[key] == 0:
#         color_map_2010[key] = "blue"
#     elif color_map_2010[key] == -1:
#         color_map_2010[key] = "red"
#
# rel_colors_2010 = [color_map_2010.get(edge) for edge in G[12].edges()]
# pos_2010 = nx.spectral_layout(G[12])
# nx.draw(G[12], pos_2010, with_labels=True, edge_color=rel_colors_2010)
# plt.savefig("static/graph/G2010.png")
# plt.close()


# G[13] = nx.Graph()
# df = pd.read_excel(f"Files/F2011.xlsx")
# G[13] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2011 = number_of_nodes(G[13])
# print(f"2011: {count_2011}")
# edges_2011 = number_of_edges(G[13])
# print(f"2011_edges: {edges_2011}")
# rel_count_2011 = nx.get_edge_attributes(G[13], "relationship")
# peer_2011 = 0
# provider_2011 = 0
# for key in rel_count_2011:
#     if rel_count_2011[key] == 0:
#         peer_2011 += 1
#     elif rel_count_2011[key] == -1:
#         provider_2011 += 1
#
# print(f"peer_2011: {peer_2011}")
# print(f"provider_2011: {provider_2011}")
#
# density_2011 = nx.density(G[13])
# print(f"density_2011: {density_2011}")

# color_map_2011 = nx.get_edge_attributes(G[13], "relationship")
#
# for key in color_map_2011:
#     if color_map_2011[key] == 0:
#         color_map_2011[key] = "blue"
#     elif color_map_2011[key] == -1:
#         color_map_2011[key] = "red"
#
# rel_colors_2011 = [color_map_2011.get(edge) for edge in G[13].edges()]
# pos_2011 = nx.spectral_layout(G[13])
# nx.draw(G[13], pos_2011, with_labels=True, edge_color=rel_colors_2011)
# plt.savefig("static/graph/G2011.png")
# plt.close()


# G[14] = nx.Graph()
# df = pd.read_excel(f"Files/F2012.xlsx")
# G[14] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2012 = number_of_nodes(G[14])
# print(f"2012: {count_2012}")
# edges_2012 = number_of_edges(G[14])
# print(f"2012_edges: {edges_2012}")
# rel_count_2012 = nx.get_edge_attributes(G[14], "relationship")
# peer_2012 = 0
# provider_2012 = 0
# for key in rel_count_2012:
#     if rel_count_2012[key] == 0:
#         peer_2012 += 1
#     elif rel_count_2012[key] == -1:
#         provider_2012 += 1
#
# print(f"peer_2012: {peer_2012}")
# print(f"provider_2012: {provider_2012}")
#
# density_2012 = nx.density(G[14])
# print(f"density_2012: {density_2012}")

# color_map_2012 = nx.get_edge_attributes(G[14], "relationship")
#
# for key in color_map_2012:
#     if color_map_2012[key] == 0:
#         color_map_2012[key] = "blue"
#     elif color_map_2012[key] == -1:
#         color_map_2012[key] = "red"
#
# rel_colors_2012 = [color_map_2012.get(edge) for edge in G[14].edges()]
# pos_2012 = nx.spectral_layout(G[14])
# nx.draw(G[14], pos_2012, with_labels=True, edge_color=rel_colors_2012)
# plt.savefig("static/graph/G2012.png")
# plt.close()


# G[15] = nx.Graph()
# df = pd.read_excel(f"Files/F2013.xlsx")
# G[15] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2013 = number_of_nodes(G[15])
# print(f"2013: {count_2013}")
# edges_2013 = number_of_edges(G[15])
# print(f"2013_edges: {edges_2013}")
# rel_count_2013 = nx.get_edge_attributes(G[15], "relationship")
# peer_2013 = 0
# provider_2013 = 0
# for key in rel_count_2013:
#     if rel_count_2013[key] == 0:
#         peer_2013 += 1
#     elif rel_count_2013[key] == -1:
#         provider_2013 += 1
#
# print(f"peer_2013: {peer_2013}")
# print(f"provider_2013: {provider_2013}")
#
# density_2013 = nx.density(G[15])
# print(f"density_2013: {density_2013}")

# color_map_2013 = nx.get_edge_attributes(G[15], "relationship")
#
# for key in color_map_2013:
#     if color_map_2013[key] == 0:
#         color_map_2013[key] = "blue"
#     elif color_map_2013[key] == -1:
#         color_map_2013[key] = "red"
#
# rel_colors_2013 = [color_map_2013.get(edge) for edge in G[15].edges()]
# pos_2013 = nx.spectral_layout(G[15])
# nx.draw(G[15], pos_2013, with_labels=True, edge_color=rel_colors_2013)
# plt.savefig("static/graph/G2013.png")
# plt.close()


# G[16] = nx.Graph()
# df = pd.read_excel(f"Files/F2014.xlsx")
# G[16] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2014 = number_of_nodes(G[16])
# print(f"2014: {count_2014}")
# edges_2014 = number_of_edges(G[16])
# print(f"2014_edges: {edges_2014}")
# rel_count_2014 = nx.get_edge_attributes(G[16], "relationship")
# peer_2014 = 0
# provider_2014 = 0
# for key in rel_count_2014:
#     if rel_count_2014[key] == 0:
#         peer_2014 += 1
#     elif rel_count_2014[key] == -1:
#         provider_2014 += 1
#
# print(f"peer_2014: {peer_2014}")
# print(f"provider_2014: {provider_2014}")
#
# density_2014 = nx.density(G[16])
# print(f"density_2014: {density_2014}")

# color_map_2014 = nx.get_edge_attributes(G[16], "relationship")
#
# for key in color_map_2014:
#     if color_map_2014[key] == 0:
#         color_map_2014[key] = "blue"
#     elif color_map_2014[key] == -1:
#         color_map_2014[key] = "red"
#
# rel_colors_2014 = [color_map_2014.get(edge) for edge in G[16].edges()]
# pos_2014 = nx.spectral_layout(G[16])
# nx.draw(G[16], pos_2014, with_labels=True, edge_color=rel_colors_2014)
# plt.savefig("static/graph/G2014.png")
# plt.close()


# G[17] = nx.Graph()
# df = pd.read_excel(f"Files/F2015.xlsx")
# G[17] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2015 = number_of_nodes(G[17])
# print(f"2015: {count_2015}")
# edges_2015 = number_of_edges(G[17])
# print(f"2015_edges: {edges_2015}")
# rel_count_2015 = nx.get_edge_attributes(G[17], "relationship")
# peer_2015 = 0
# provider_2015 = 0
# for key in rel_count_2015:
#     if rel_count_2015[key] == 0:
#         peer_2015 += 1
#     elif rel_count_2015[key] == -1:
#         provider_2015 += 1
#
# print(f"peer_2015: {peer_2015}")
# print(f"provider_2015: {provider_2015}")
#
# density_2015 = nx.density(G[17])
# print(f"density_2015: {density_2015}")

# color_map_2015 = nx.get_edge_attributes(G[17], "relationship")
#
# for key in color_map_2015:
#     if color_map_2015[key] == 0:
#         color_map_2015[key] = "blue"
#     elif color_map_2015[key] == -1:
#         color_map_2015[key] = "red"
#
# rel_colors_2015 = [color_map_2015.get(edge) for edge in G[17].edges()]
# pos_2015 = nx.spectral_layout(G[17])
# nx.draw(G[17], pos_2015, with_labels=True, edge_color=rel_colors_2015)
# plt.savefig("static/graph/G2015.png")
# plt.close()


# G[18] = nx.Graph()
# df = pd.read_excel(f"Files/F2016.xlsx")
# G[18] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2016 = number_of_nodes(G[18])
# print(f"2016: {count_2016}")
# edges_2016 = number_of_edges(G[18])
# print(f"2016_edges: {edges_2016}")
# rel_count_2016 = nx.get_edge_attributes(G[18], "relationship")
# peer_2016 = 0
# provider_2016 = 0
# for key in rel_count_2016:
#     if rel_count_2016[key] == 0:
#         peer_2016 += 1
#     elif rel_count_2016[key] == -1:
#         provider_2016 += 1
#
# print(f"peer_2016: {peer_2016}")
# print(f"provider_2016: {provider_2016}")
#
# density_2016 = nx.density(G[18])
# print(f"density_2016: {density_2016}")

# color_map_2016 = nx.get_edge_attributes(G[18], "relationship")
#
# for key in color_map_2016:
#     if color_map_2016[key] == 0:
#         color_map_2016[key] = "blue"
#     elif color_map_2016[key] == -1:
#         color_map_2016[key] = "red"
#
# rel_colors_2016 = [color_map_2016.get(edge) for edge in G[18].edges()]
# pos_2016 = nx.spectral_layout(G[18])
# nx.draw(G[18], pos_2016, with_labels=True, edge_color=rel_colors_2016)
# plt.savefig("static/graph/G2016.png")
# plt.close()


# G[19] = nx.Graph()
# df = pd.read_excel(f"Files/F2017.xlsx")
# G[19] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2017 = number_of_nodes(G[19])
# print(f"2017: {count_2017}")
# edges_2017 = number_of_edges(G[19])
# print(f"2017_edges: {edges_2017}")
# rel_count_2017 = nx.get_edge_attributes(G[19], "relationship")
# peer_2017 = 0
# provider_2017 = 0
# for key in rel_count_2017:
#     if rel_count_2017[key] == 0:
#         peer_2017 += 1
#     elif rel_count_2017[key] == -1:
#         provider_2017 += 1
#
# print(f"peer_2017: {peer_2017}")
# print(f"provider_2017: {provider_2017}")
#
# density_2017 = nx.density(G[19])
# print(f"density_2017: {density_2017}")

# color_map_2017 = nx.get_edge_attributes(G[19], "relationship")
#
# for key in color_map_2017:
#     if color_map_2017[key] == 0:
#         color_map_2017[key] = "blue"
#     elif color_map_2017[key] == -1:
#         color_map_2017[key] = "red"
#
# rel_colors_2017 = [color_map_2017.get(edge) for edge in G[19].edges()]
# pos_2017 = nx.spectral_layout(G[19])
# nx.draw(G[19], pos_2017, with_labels=True, edge_color=rel_colors_2017)
# plt.savefig("static/graph/G2017.png")
# plt.close()


# G[20] = nx.Graph()
# df = pd.read_excel(f"Files/F2018.xlsx")
# G[20] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2018 = number_of_nodes(G[20])
# print(f"2018: {count_2018}")
# edges_2018 = number_of_edges(G[20])
# print(f"2018_edges: {edges_2018}")
# rel_count_2018 = nx.get_edge_attributes(G[20], "relationship")
# peer_2018 = 0
# provider_2018 = 0
# for key in rel_count_2018:
#     if rel_count_2018[key] == 0:
#         peer_2018 += 1
#     elif rel_count_2018[key] == -1:
#         provider_2018 += 1
#
# print(f"peer_2018: {peer_2018}")
# print(f"provider_2018: {provider_2018}")
#
# density_2018 = nx.density(G[20])
# print(f"density_2018: {density_2018}")

# color_map_2018 = nx.get_edge_attributes(G[20], "relationship")
#
# for key in color_map_2018:
#     if color_map_2018[key] == 0:
#         color_map_2018[key] = "blue"
#     elif color_map_2018[key] == -1:
#         color_map_2018[key] = "red"
#
# rel_colors_2018 = [color_map_2018.get(edge) for edge in G[20].edges()]
# pos_2018 = nx.spectral_layout(G[20])
# nx.draw(G[20], pos_2018, with_labels=True, edge_color=rel_colors_2018)
# plt.savefig("static/graph/G2018.png")
# plt.close()


# G[21] = nx.Graph()
# df = pd.read_excel(f"Files/F2019.xlsx")
# G[21] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2019 = number_of_nodes(G[21])
# print(f"2019: {count_2019}")
# edges_2019 = number_of_edges(G[21])
# print(f"2019_edges: {edges_2019}")
# rel_count_2019 = nx.get_edge_attributes(G[21], "relationship")
# peer_2019 = 0
# provider_2019 = 0
# for key in rel_count_2019:
#     if rel_count_2019[key] == 0:
#         peer_2019 += 1
#     elif rel_count_2019[key] == -1:
#         provider_2019 += 1
#
# print(f"peer_2019: {peer_2019}")
# print(f"provider_2019: {provider_2019}")
#
# density_2019 = nx.density(G[21])
# print(f"density_2019: {density_2019}")

# color_map_2019 = nx.get_edge_attributes(G[21], "relationship")
#
# for key in color_map_2019:
#     if color_map_2019[key] == 0:
#         color_map_2019[key] = "blue"
#     elif color_map_2019[key] == -1:
#         color_map_2019[key] = "red"
#
# rel_colors_2019 = [color_map_2019.get(edge) for edge in G[21].edges()]
# pos_2019 = nx.spectral_layout(G[21])
# nx.draw(G[21], pos_2019, with_labels=True, edge_color=rel_colors_2019)
# plt.savefig("static/graph/G2019.png")
# plt.close()


# G[22] = nx.Graph()
# df = pd.read_excel(f"Files/F2020.xlsx")
# G[22] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2020 = number_of_nodes(G[22])
# print(f"2020: {count_2020}")
# edges_2020 = number_of_edges(G[22])
# print(f"2020_edges: {edges_2020}")
# rel_count_2020 = nx.get_edge_attributes(G[22], "relationship")
# peer_2020 = 0
# provider_2020 = 0
# for key in rel_count_2020:
#     if rel_count_2020[key] == 0:
#         peer_2020 += 1
#     elif rel_count_2020[key] == -1:
#         provider_2020 += 1
#
# print(f"peer_2020: {peer_2020}")
# print(f"provider_2020: {provider_2020}")
#
# density_2020 = nx.density(G[22])
# print(f"density_2020: {density_2020}")

# color_map_2020 = nx.get_edge_attributes(G[22], "relationship")
#
# for key in color_map_2020:
#     if color_map_2020[key] == 0:
#         color_map_2020[key] = "blue"
#     elif color_map_2020[key] == -1:
#         color_map_2020[key] = "red"
#
# rel_colors_2020 = [color_map_2020.get(edge) for edge in G[22].edges()]
# pos_2020 = nx.spectral_layout(G[22])
# nx.draw(G[22], pos_2020, with_labels=True, edge_color=rel_colors_2020)
# plt.savefig("static/graph/G2020.png")
# plt.close()


# G[23] = nx.Graph()
# df = pd.read_excel(f"Files/F2021.xlsx")
# G[23] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2021 = number_of_nodes(G[23])
# print(f"2021: {count_2021}")
# edges_2021 = number_of_edges(G[23])
# print(f"2021_edges: {edges_2021}")
# rel_count_2021 = nx.get_edge_attributes(G[23], "relationship")
# peer_2021 = 0
# provider_2021 = 0
# for key in rel_count_2021:
#     if rel_count_2021[key] == 0:
#         peer_2021 += 1
#     elif rel_count_2021[key] == -1:
#         provider_2021 += 1
#
# print(f"peer_2021: {peer_2021}")
# print(f"provider_2021: {provider_2021}")
#
# density_2021 = nx.density(G[23])
# print(f"density_2021: {density_2021}")

# color_map_2021 = nx.get_edge_attributes(G[23], "relationship")
#
# for key in color_map_2021:
#     if color_map_2021[key] == 0:
#         color_map_2021[key] = "blue"
#     elif color_map_2021[key] == -1:
#         color_map_2021[key] = "red"
#
# rel_colors_2021 = [color_map_2021.get(edge) for edge in G[23].edges()]
# pos_2021 = nx.spectral_layout(G[23])
# nx.draw(G[23], pos_2021, with_labels=True, edge_color=rel_colors_2021)
# plt.savefig("static/graph/G2021.png")
# plt.close()


# G[24] = nx.Graph()
# df = pd.read_excel(f"Files/F2022.xlsx")
# G[24] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2022 = number_of_nodes(G[24])
# print(f"2022: {count_2022}")
# edges_2022 = number_of_edges(G[24])
# print(f"2022_edges: {edges_2022}")
# rel_count_2022 = nx.get_edge_attributes(G[24], "relationship")
# peer_2022 = 0
# provider_2022 = 0
# for key in rel_count_2022:
#     if rel_count_2022[key] == 0:
#         peer_2022 += 1
#     elif rel_count_2022[key] == -1:
#         provider_2022 += 1
#
# print(f"peer_2022: {peer_2022}")
# print(f"provider_2022: {provider_2022}")
#
# density_2022 = nx.density(G[24])
# print(f"density_2022: {density_2022}")

# color_map_2022 = nx.get_edge_attributes(G[24], "relationship")
#
# for key in color_map_2022:
#     if color_map_2022[key] == 0:
#         color_map_2022[key] = "blue"
#     elif color_map_2022[key] == -1:
#         color_map_2022[key] = "red"
#
# rel_colors_2022 = [color_map_2022.get(edge) for edge in G[24].edges()]
# pos_2022 = nx.spectral_layout(G[24])
# nx.draw(G[24], pos_2022, with_labels=True, edge_color=rel_colors_2022)
# plt.savefig("static/graph/G2022.png")
# plt.close()

## PLOTS THE AS COUNT GRPAH BY YEAR
# x = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
#      2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
# y = [count_1998, count_1999, count_2000, count_2001, count_2002, count_2003, count_2004, count_2005, count_2006,
#      count_2007, count_2008, count_2009, count_2010, count_2011, count_2012, count_2013, count_2014, count_2015,
#      count_2016, count_2017, count_2018, count_2019, count_2020, count_2021, count_2022]
# plt.plot(x, y)
# plt.title("Autonomous System Count (1998-2022)")
# plt.xticks(x, rotation="vertical")
# plt.grid(True)
# plt.savefig("static/yearly_count.png")
# plt.close()
#
## PLOTS BOTH THE AS COUNT AND DENSITY PROPERTY OF THE GRAPH BY YEAR IN ONE CHART
# x4 = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
#       2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
# y4 = [density_1998, density_1999, density_2000, density_2001, density_2002, density_2003, density_2004,
#       density_2005, density_2006, density_2007, density_2008, density_2009, density_2010, density_2011,
#       density_2012, density_2013, density_2014, density_2015, density_2016, density_2017, density_2018,
#       density_2019, density_2020, density_2021, density_2022]
# plt.plot(x4, y4)
# plt.title("Network Density (1998-2022)")
# plt.xticks(x4, rotation="vertical")
# plt.grid(True)
# plt.savefig("static/density.png")
# plt.close()

## PLOTS THE TOTAL NUMBER OF EDGES, THE COUNT OF EDGES TAGGED AS PROVIDER-CUSTOMER,
## AND THE COUNT OF EDGES TAGGED AS PEER-PEER BY YEAR ON ONE CHART
# x1 = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
#       2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
# y1 = [edges_1998, edges_1999, edges_2000, edges_2001, edges_2002, edges_2003, edges_2004, edges_2005, edges_2006,
#       edges_2007, edges_2008, edges_2009, edges_2010, edges_2011, edges_2012, edges_2013, edges_2014, edges_2015,
#       edges_2016, edges_2017, edges_2018, edges_2019, edges_2020, edges_2021, edges_2022]
# y2 = [provider_1998, provider_1999, provider_2000, provider_2001, provider_2002, provider_2003, provider_2004,
#       provider_2005, provider_2006, provider_2007, provider_2008, provider_2009, provider_2010, provider_2011,
#       provider_2012, provider_2013, provider_2014, provider_2015, provider_2016, provider_2017, provider_2018,
#       provider_2019, provider_2020, provider_2021, provider_2022]
# y3 = [peer_1998, peer_1999, peer_2000, peer_2001, peer_2002, peer_2003, peer_2004, peer_2005, peer_2006,
#       peer_2007, peer_2008, peer_2009, peer_2010, peer_2011, peer_2012, peer_2013, peer_2014, peer_2015,
#       peer_2016, peer_2017, peer_2018, peer_2019, peer_2020, peer_2021, peer_2022]
# fig, ax = plt.subplots()
# ax.plot(x1, y1, color="green", label="All")
# ax.plot(x1, y2, color="red", label="Provider-Customer")
# ax.plot(x1, y3, color="blue", label="Peer-Peer")
# plt.title("Autonomous System Relationships (1998-2022)")
# plt.xticks(x1, rotation="vertical")
# plt.grid(True)
# ax.legend(loc="upper left")
# plt.savefig("static/relationship.png")
# plt.close()


## PLOTS THE COUNT OF NODES WHICH WERE ADDED AND REMOVED BETWEEN 2 CONSECUTIVE YEARS
# # ADDED
# new1 = []
# node0 = G[0].nodes()
# node1 = G[1].nodes()
# for n in node1:
#     if n not in node0:
#         new1.append(n)
# output1 = len(new1)
#
# new2 = []
# node2 = G[2].nodes()
# for n in node2:
#     if n not in node1:
#         new2.append(n)
# output2 = len(new2)
#
# new3 = []
# node3 = G[3].nodes()
# for n in node3:
#     if n not in node2:
#         new3.append(n)
# output3 = len(new3)
#
# new4 = []
# node4 = G[4].nodes()
# for n in node4:
#     if n not in node3:
#         new4.append(n)
# output4 = len(new4)
#
# new5 = []
# node5 = G[5].nodes()
# for n in node5:
#     if n not in node4:
#         new5.append(n)
# output5 = len(new5)
#
# new6 = []
# node6 = G[6].nodes()
# for n in node6:
#     if n not in node5:
#         new6.append(n)
# output6 = len(new6)
#
# new7 = []
# node7 = G[7].nodes()
# for n in node7:
#     if n not in node6:
#         new7.append(n)
# output7 = len(new7)
#
# new8 = []
# node8 = G[8].nodes()
# for n in node8:
#     if n not in node7:
#         new8.append(n)
# output8 = len(new8)
#
# new9 = []
# node9 = G[9].nodes()
# for n in node9:
#     if n not in node8:
#         new9.append(n)
# output9 = len(new9)
#
# new10 = []
# node10 = G[10].nodes()
# for n in node10:
#     if n not in node9:
#         new10.append(n)
# output10 = len(new10)
#
# new11 = []
# node11 = G[11].nodes()
# for n in node11:
#     if n not in node10:
#         new11.append(n)
# output11 = len(new11)
#
# new12 = []
# node12 = G[12].nodes()
# for n in node12:
#     if n not in node11:
#         new12.append(n)
# output12 = len(new12)
#
# new13 = []
# node13 = G[13].nodes()
# for n in node13:
#     if n not in node12:
#         new13.append(n)
# output13 = len(new13)
#
# new14 = []
# node14 = G[14].nodes()
# for n in node14:
#     if n not in node13:
#         new14.append(n)
# output14 = len(new14)
#
# new15 = []
# node15 = G[15].nodes()
# for n in node15:
#     if n not in node14:
#         new15.append(n)
# output15 = len(new15)
#
# new16 = []
# node16 = G[16].nodes()
# for n in node16:
#     if n not in node15:
#         new16.append(n)
# output16 = len(new16)
#
# new17 = []
# node17 = G[17].nodes()
# for n in node17:
#     if n not in node16:
#         new17.append(n)
# output17 = len(new17)
#
# new18 = []
# node18 = G[18].nodes()
# for n in node18:
#     if n not in node17:
#         new18.append(n)
# output18 = len(new18)
#
# new19 = []
# node19 = G[19].nodes()
# for n in node19:
#     if n not in node18:
#         new19.append(n)
# output19 = len(new19)
#
# new20 = []
# node20 = G[20].nodes()
# for n in node20:
#     if n not in node19:
#         new20.append(n)
# output20 = len(new20)
#
# new21 = []
# node21 = G[21].nodes()
# for n in node21:
#     if n not in node20:
#         new21.append(n)
# output21 = len(new21)
#
# new22 = []
# node22 = G[22].nodes()
# for n in node22:
#     if n not in node21:
#         new22.append(n)
# output22 = len(new22)
#
# new23 = []
# node23 = G[23].nodes()
# for n in node23:
#     if n not in node22:
#         new23.append(n)
# output23 = len(new23)
#
# new24 = []
# node24 = G[24].nodes()
# for n in node24:
#     if n not in node23:
#         new24.append(n)
# output24 = len(new24)
#
# # REMOVED
# removed0 = []
# for n in node0:
#     if n not in node1:
#         removed0.append(n)
#
# result0 = len(removed0)
#
# removed1 = []
# for n in node1:
#     if n not in node2:
#         removed1.append(n)
#
# result1 = len(removed1)
#
# removed2 = []
# for n in node2:
#     if n not in node3:
#         removed2.append(n)
#
# result2 = len(removed2)
#
# removed3 = []
# for n in node3:
#     if n not in node4:
#         removed3.append(n)
#
# result3 = len(removed3)
#
# removed4 = []
# for n in node4:
#     if n not in node5:
#         removed4.append(n)
#
# result4 = len(removed4)
#
# removed5 = []
# for n in node5:
#     if n not in node6:
#         removed5.append(n)
#
# result5 = len(removed5)
#
# removed6 = []
# for n in node6:
#     if n not in node7:
#         removed6.append(n)
#
# result6 = len(removed6)
#
# removed7 = []
# for n in node7:
#     if n not in node8:
#         removed7.append(n)
#
# result7 = len(removed7)
#
# removed8 = []
# for n in node8:
#     if n not in node9:
#         removed8.append(n)
#
# result8 = len(removed8)
#
# removed9 = []
# for n in node9:
#     if n not in node10:
#         removed9.append(n)
#
# result9 = len(removed9)
#
# removed10 = []
# for n in node10:
#     if n not in node11:
#         removed10.append(n)
#
# result10 = len(removed10)
#
# removed11 = []
# for n in node11:
#     if n not in node12:
#         removed11.append(n)
#
# result11 = len(removed11)
#
# removed12 = []
# for n in node12:
#     if n not in node13:
#         removed12.append(n)
#
# result12 = len(removed12)
#
# removed13 = []
# for n in node13:
#     if n not in node14:
#         removed13.append(n)
#
# result13 = len(removed13)
#
# removed14 = []
# for n in node14:
#     if n not in node15:
#         removed14.append(n)
#
# result14 = len(removed14)
#
# removed15 = []
# for n in node15:
#     if n not in node16:
#         removed15.append(n)
#
# result15 = len(removed15)
#
# removed16 = []
# for n in node16:
#     if n not in node17:
#         removed16.append(n)
#
# result16 = len(removed16)
#
# removed17 = []
# for n in node17:
#     if n not in node18:
#         removed17.append(n)
#
# result17 = len(removed17)
#
# removed18 = []
# for n in node18:
#     if n not in node19:
#         removed18.append(n)
#
# result18 = len(removed18)
#
# removed19 = []
# for n in node19:
#     if n not in node20:
#         removed19.append(n)
#
# result19 = len(removed19)
#
# removed20 = []
# for n in node20:
#     if n not in node21:
#         removed20.append(n)
#
# result20 = len(removed20)
#
# removed21 = []
# for n in node21:
#     if n not in node22:
#         removed21.append(n)
#
# result21 = len(removed21)
#
# removed22 = []
# for n in node22:
#     if n not in node23:
#         removed22.append(n)
#
# result22 = len(removed22)
#
# removed23 = []
# for n in node23:
#     if n not in node24:
#         removed23.append(n)
#
# result23 = len(removed23)
#
# # PLOTS
# x5 = ["'98-'99", "'99-'00", "'00-'01", "'01-'02", "'02-'03", "'03-'04", "'04-'05", "'05-'06", "'06-'07", "'07-'08",
#       "'08-'09", "'09-'10", "'10-'11", "'11-'12", "'12-'13", "'13-'14", "'14-'15", "'15-'16", "'16-'17", "'17-'18",
#       "'18-'19", "'19-'20", "'20-'21", "'21-'22"]
# y5 = [output1, output2, output3, output4, output5, output6, output7, output8, output9, output10, output11, output12,
#       output13, output14, output15, output16, output17, output18, output19, output20, output21, output22, output23, output24]
# y6 = [result0, result1, result2, result3, result4, result5, result6, result7, result8, result9, result10, result11,
#       result12, result13, result14, result15, result16, result17, result18, result19, result20, result21, result22, result23]
# fig, ax = plt.subplots(figsize=(10, 6))
# ax.plot(x5, y5, color="blue", label="Added ASs")
# ax.plot(x5, y6, color="red", label="Removed ASs")
# plt.title("Added/Removed Autonomous Systems (1998-2022)")
# plt.xticks(x5, rotation="vertical")
# plt.grid(True)
# ax.legend(loc="upper left")
# plt.savefig("static/add_remove.png")
# plt.close()

# G = [1998, 1999, 2000]
# date = 1998
# index = int(get_index_of_date(G, date))
#
# F = [1998, 1999, 2000]
# file_index = int(get_index_of_file(F, date))
#
# F = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
    #      2016, 2017, 2018, 2019, 2020, 2021, 2022]
    # date = int(form_output["Period"])
    # file_index = int(get_index_of_file(F, date))
    # F[file_index] = f"Files/F{date}.xlsx"
    # G[index].add_edges_from(file_upload(F[file_index]).edges)
# # 1998
# F[0] = f"Files/F{date}.xls"
# file = F[0]
# G[0] = nx.DiGraph()
# G[0].add_edges_from(file_upload(F[0]).edges)  # THE EDGES IN THE DATASET ARE ADDED TO THE DIRECTED GRAPH, G
#
#
# # THE FOLLOWING BLOCK OF CODE CALCULATES THE CENTRALITY MEASURES OF THE NODES IN THE NETWORK AND THE NETWORK AS A WHOLE
# degree1998 = dict(G[0].degree)
# in_degree1998 = dict(G[0].in_degree)
# out_degree1998 = dict(G[0].out_degree)
# btw_c1998 = nx.betweenness_centrality(G[0])
# eigen_c1998 = nx.eigenvector_centrality(G[0])
# nx.set_node_attributes(G[0], degree1998, 'Degree')
# nx.set_node_attributes(G[0], in_degree1998, 'In-degree')
# nx.set_node_attributes(G[0], out_degree1998, 'Out-degree')
# nx.set_node_attributes(G[0], btw_c1998, 'Betweenness')
# nx.set_node_attributes(G[0], eigen_c1998, 'Eigenvector')
#
# color_map = nx.get_edge_attributes(G[0], "rel")
#
# for key in color_map:
#     if color_map[key] == "-1":
#         color_map[key] = "red"
#     if color_map[key] == "0":
#         color_map[key] = "blue"
#
# rel_colors = [color_map.get(edge) for edge in G[0].edges()]
# # node_sizes = [(total_domains.count(node)*100) for node in G[0].nodes()]
# pos = nx.spectral_layout(G[0])
# # nx.draw(G[0], pos, with_labels=True, edge_color=rel_colors)
# # plt.show()
#
# # 1999
# F[1] = f"Files/F{date}.xls"
# G[1] = nx.DiGraph()
# G[1].add_edges_from(file_upload(F[1]).edges)


# THE FOLLOWING BLOCK OF CODE CALCULATES THE CENTRALITY MEASURES OF THE NODES IN THE NETWORK AND THE NETWORK AS A WHOLE
# degree1999 = dict(G1999.degree)
# in_degree1999 = dict(G1999.in_degree)
# out_degree1999 = dict(G1999.out_degree)
# btw_c1999 = nx.betweenness_centrality(G1999)
# eigen_c1999 = nx.eigenvector_centrality(G1999)
# nx.set_node_attributes(G1999, degree1999, 'Degree')
# nx.set_node_attributes(G1999, in_degree1999, 'In-degree')
# nx.set_node_attributes(G1999, out_degree1999, 'Out-degree')
# nx.set_node_attributes(G1999, btw_c1999, 'Betweenness')
# nx.set_node_attributes(G1999, eigen_c1999, 'Eigenvector')

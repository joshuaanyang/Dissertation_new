# IMPORT THE PACKAGES REQUIRED
from flask import Flask, render_template, request
import networkx as nx
from operator import itemgetter
from networkx import number_of_nodes
from Documents import get_index_of_date
import pandas as pd
import itertools
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')


app = Flask(__name__)  # INITIALISE THE APP FROM THE FLASK CLASS


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")  # RETURNS THE TEMPLATE STORED IN THE PARENTHESIS


@app.route("/TopologyProperties", methods=["GET", "POST"])
def topologyproperties():
    return render_template("TopologyProperties.html")


@app.route("/CentralNodes", methods=["GET", "POST"])
def centralnodes():
    return render_template("CentralNodes.html")


@app.route("/DomainHierarchy", methods=["GET", "POST"])
def domainhierarchy():
    return render_template("DomainHierarchy.html")


@app.route("/DomainCount", methods=["GET", "POST"])
def domaincount():
    return render_template("DomainCountPerPeriod.html")


@app.route("/NewDomains", methods=["GET", "POST"])
def newdomains():
    return render_template("NewDomainPerPeriod.html")


@app.route("/RemovedDomains", methods=["GET", "POST"])
def olddomains():
    return render_template("RemovedDomainPerPeriod.html")


# COMPUTES THE TOP NODES BASED ON CENTRALITY MEASURES
# THE METHODS POST AND GET ARE REQUIRED TO GET THE OUTPUTS OF THE FORM AND TO ALSO POST RESULTS TO THE HTML SCRIPT
@app.route("/CNresult", methods=["POST", "GET"])
def centralnodesresult():
    form_output = request.form.to_dict()  # EXTRACTS THE DATA FROM THE FORMS ON THE WEBPAGE
    date = int(form_output["Period"])  # passes the input named "period" into a variable "date"

    G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022]  # LIST OF ALL THE YEARS AVAILABLE ON THE FORM
    index = int(get_index_of_date(G, date))  # GETS THE INDEX OF THE YEAR IN THE DATE VARIABLE FROM THE LIST G

    G[index] = nx.Graph()  # NETWORKX IS USED TO CREATE AN UNDIRECTED GRAPH FOR THAT YEAR

    # PANDAS IS USED TO EXTRACT THE DATA FROM THE FILE
    # THE DATA IS EXTRACTED FROM THE PANDAS DATAFRAME AND PASSED INTO THE UNDIRECTED GRAPH
    # NODE1 IN THE FILE IS STORED IN THE COLUMN TITLED "SOURCE"
    # NODE2 IN THE FILE IS STORED IN THE COLUMN TITLED "TARGET"
    # THE RELATIONSHIP TYPES ARE STORED IN THE COLUMN TITLED "RELATIONSHIP"
    df = pd.read_excel(f"Files/F{date}.xlsx")
    G[index] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')

    # COMPUTES THE CENTRALITY MEASURES OF THE NODES AND SAVES THEM AS ATTRIBUTES OF THE NODES
    deg_c = dict(G[index].degree)
    btw_c = nx.betweenness_centrality(G[index])
    eigen_c = nx.eigenvector_centrality(G[index])
    nx.set_node_attributes(G[index], deg_c, 'Degree')
    nx.set_node_attributes(G[index], btw_c, 'Betweenness')
    nx.set_node_attributes(G[index], eigen_c, 'Eigenvector')

    # SORTS THE NODES BY THEIR CENTRALITY MEASURES IN AN ASCENDING MANNER
    degree = sorted(deg_c.items(), key=itemgetter(1), reverse=True)
    len_d = len(degree[:10])
    eigen = sorted(eigen_c.items(), key=itemgetter(1), reverse=True)
    len_e = len(eigen[:10])
    btw = sorted(btw_c.items(), key=itemgetter(1), reverse=True)
    len_b = len(btw[:10])

    # THE DATE, CENTRALITY MEASURES VARIABLES WITH A LIMIT OF 10 ARE PASSED
    # INTO PLACEHOLDERS ON THE WEBPAGE AS THE OUTPUT
    return render_template("CNresult.html", date=date, degree=degree[:10], len_d=len_d, eigen=eigen[:10], len_e=len_e, btw=btw[:10], len_b=len_b,)


# COMPUTES THE TIER AND TOPOLOGY PROPERTIES OF THE AS
@app.route("/TPresult", methods=["POST", "GET"])
def tpresult():
    form_output = request.form.to_dict()
    domain = int(form_output["domainID"])
    date = int(form_output["Period"])
    G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022]
    index = int(get_index_of_date(G, date))
    G[index] = nx.DiGraph()
    date = int(form_output["Period"])
    df = pd.read_excel(f"files/F{date}.xlsx")
    G[index] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship',
                                       create_using=nx.DiGraph())

    error_statement = f"Oops! AS {domain} DOES NOT EXIST IN {date}."
    if domain not in G[index].nodes():
        attributes = error_statement
        attributes_h = error_statement
    else:
        degree = dict(G[index].degree)
        btw_c = nx.betweenness_centrality(G[index])
        eigen_c = nx.eigenvector_centrality(G[index])
        nx.set_node_attributes(G[index], degree, 'Degree')
        nx.set_node_attributes(G[index], btw_c, 'Betweenness')
        nx.set_node_attributes(G[index], eigen_c, 'Eigenvector')
        attributes = dict(G[index].nodes[domain])

        H = nx.DiGraph()  # NETWORKX IS USED TO CREATE A DIRECTED GRAPH, H

        # EDGES WITH RELATIONSHIP ATTRIBUTES OF "-1" ARE PASSED INTO THE H GRAPH
        for node1, node2, edge in G[index].edges(data=True):
            if edge['relationship'] == -1:
                H.add_edge(node1, node2, relationship=edge)

        in_degree = dict(H.in_degree)
        out_degree = dict(H.out_degree)
        nx.set_node_attributes(H, in_degree, 'In-degree')
        nx.set_node_attributes(H, out_degree, 'Out-degree')

        # FOR NODES IN H, THE TIER ATTRIBUTES FOR EACH ARE ASSIGNED DEPENDING ON THEIR IN-DEGREE OR OUT-DEGREE
        for n, d in H.nodes(data=True):
            if d['In-degree'] < 1:
                tier = "Tier_1"
                H.nodes[n]['Tier'] = tier
            elif d['Out-degree'] < 1:
                tier = "Tier_3"
                H.nodes[n]['Tier'] = tier
            elif d['In-degree'] >= 1 and d['Out-degree'] >= 1:
                tier = "Tier_2"
                H.nodes[n]['Tier'] = tier

        attributes_h = H.nodes[domain]["Tier"]

    # THE VARIABLES ARE PASSED INTO THEIR PLACEHOLDERS ON THE WEBPAGE AS THE COMPUTED RESULT
    return render_template("TPresult.html", domain=domain, date=date, attributes=attributes, attributes_h=attributes_h)


# COMPUTES THE NEIGHBOURS OF A NODE
@app.route("/DHresult", methods=["POST", "GET"])
def dhresult():
    # CHECKS IF THE FILENAME EXISTS, IF YES, THE FILE IS DELETED
    file_name = "static/images/graph.png"
    if os.path.isfile(file_name):
        os.remove(file_name)

    form_output = request.form.to_dict()
    domain = int(form_output["domainID"])
    date = int(form_output["Period"])
    c_degree = int(form_output["cutoff"])
    G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022]
    index = int(get_index_of_date(G, date))
    G[index] = nx.Graph()
    date = int(form_output["Period"])
    df = pd.read_excel(f"Files/F{date}.xlsx")
    G[index] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship',
                                       create_using=nx.Graph())

    error_statement = f"Oops! AS {domain} DOES NOT EXIST IN {date}."
    if domain not in G[index].nodes():
        path = error_statement
    else:
        # A PATH LIST IS CREATED TO STORE THE NODES, PATH[1:] KEEPS ALL NODES EXCEPT THE FIRST ONE WHICH CREATES A SELF-LOOP
        path = []
        path.append(nx.single_source_shortest_path(G[index], domain, c_degree))  # C_DEGREE STORES THE HOP CUT-OFF FOR LINKS
        path = [tuple(val) for dic in path for key, val in dic.items()]
        path = path[1:]
        len_p = len(path)
        # AN UNDIRECTED GRAPH P IS CREATED TO PLOT THE LINKS AND NODES IN THE PATH LIST
        P = nx.Graph()
        for node_tuple in path:
            P.add_edges_from(itertools.combinations(node_tuple, 2))

        rel_attr = []
        for x in range(len_p):
            rel_attr.append(G[index][path[x][0]][path[x][1]]["relationship"])

        # EDGE COLORS ARE ASSIGNED DEPENDING ON THE RELATIONSHIP ATTRIBUTE VALUE
        color_map = nx.get_edge_attributes(G[index], "relationship")

        for key in color_map:
            if color_map[key] == 0:
                color_map[key] = "blue"
            elif color_map[key] == -1:
                color_map[key] = "red"

        rel_colors = [color_map.get(edge) for edge in G[index].edges()]

        # THE GRAPH P IS GENERATED WITH A SPRING LAYOUT AND STORED IN THE VARIABLE FILE_NAME
        # PLT.CLOSE() PREVENTS THE GRAPHS FROM GENERATING A LAYERED PLOT ON THE PREVIOUSLY GENERATED PLOT
        pos = nx.spring_layout(P)
        nx.draw(P, pos, with_labels=True, edge_color=rel_colors)
        plt.savefig(file_name)
        plt.close()

    return render_template("DHresult.html", domain=domain, date=date, path=path, len_p=len_p, c_degree=c_degree,
                           rel_attr=rel_attr)


# RENDERS THE DOMAIN HIERARCHY IMAGE
@app.route("/Image")
def image():
    return render_template("Image.html")


# COMPUTES THE COUNT OF ASs WITHIN A YEAR
@app.route("/DCresult", methods=["POST", "GET"])
def dcresult():
    form_output = request.form.to_dict()
    date = int(form_output["Period"])
    file = f"static/G{date}_.png"
    G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022]
    index = int(get_index_of_date(G, date))
    G[index] = nx.Graph()
    df = pd.read_excel(f"Files/F{date}.xlsx")
    G[index] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')

    # COMPUTES THE NETWORK SIZE AND DENSITY PROPERTY OF THE GRAPH
    count = number_of_nodes(G[index])
    density = nx.density(G[index])

    return render_template("DCresult.html", date=date, count=count, density=density, image=file)


# COMPUTES THE ASs ADDED WITHIN A PERIOD
@app.route("/NDresult", methods=["POST", "GET"])
def ndresult():
    form_output = request.form.to_dict()
    date1 = int(form_output["PeriodFrom"])
    date2 = int(form_output["PeriodTo"])
    G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022]
    index1 = int(get_index_of_date(G, date1))
    G[index1] = nx.Graph()
    df = pd.read_excel(f"Files/F{date1}.xlsx")
    G[index1] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')

    index2 = int(get_index_of_date(G, date2))
    G[index2] = nx.Graph()
    df = pd.read_excel(f"Files/F{date2}.xlsx")
    G[index2] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')

    # CREATES A NEW LIST TO STORE THE NODES WHICH EXISTS IN NODE2 BUT NOT NODE1
    new = []

    node1 = G[index1].nodes()
    node2 = G[index2].nodes()
    for n in node2:
        if n not in node1:
            new.append(n)

    result = len(new)  # COUNTS THE VALUES IN THE "NEW" LIST
    count1 = number_of_nodes(G[index1])
    count2 = number_of_nodes(G[index2])
    return render_template("NDresult.html", result=result, date1=date1, date2=date2, count1=count1, count2=count2,
                           new=new)


# COMPUTES THE ASs REMOVED WITHIN A PERIOD
@app.route("/RDresult", methods=["POST", "GET"])
def rdresult():
    form_output = request.form.to_dict()
    date1 = int(form_output["PeriodFrom"])
    date2 = int(form_output["PeriodTo"])
    G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022]
    index1 = int(get_index_of_date(G, date1))
    G[index1] = nx.Graph()
    df = pd.read_excel(f"Files/F{date1}.xlsx")
    G[index1] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')

    index2 = int(get_index_of_date(G, date2))
    df = pd.read_excel(f"Files/F{date2}.xlsx")
    G[index2] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')

    # CREATES A REMOVED LIST TO STORE THE NODES WHICH EXISTS IN NODE1 BUT NOT NODE2
    removed = []
    node1 = G[index1].nodes()
    node2 = G[index2].nodes()
    for n in node1:
        if n not in node2:
            removed.append(n)

    result = len(removed)  # COUNTS THE VALUES IN THE "REMOVED" LIST
    count1 = number_of_nodes(G[index1])
    count2 = number_of_nodes(G[index2])
    return render_template("RDresult.html", result=result, date1=date1, date2=date2, count1=count1, count2=count2,
                           removed=removed)


if __name__ == '__main__':
    app.run(debug=True, port=5005)  # THE SPECIFIC PORT IS STATED

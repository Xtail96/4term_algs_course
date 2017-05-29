from graphviz import Graph, Digraph
import os.path
inf = float('inf')

def bellman_ford(graph, source, graphType):
    img_counter = 0
    def printGraph(graph, graphType, d, node, neighbour, description, outdir = 'out'):
        nonlocal img_counter
        if graphType == "directed":
            g = Digraph(format = "png")
        else:
            g = Graph(format = "png")

        font = "Arial"
        g.attr('graph', fontname=font)
        g.attr('node', fontname=font)
        g.attr('edge', fontname=font)
        g.attr(rankdir = "LR")

        for u in graph:
            for v in graph[u]: 
                color = "black"
                g.node(u, u)
                e = graph[u][v]

                # source -> node -> neighbor - green
                # source -> neighbour - red
                if(u == source and v == node) or (u == node and v == neighbour):
                    color = "green"
                elif u == source and v == neighbour:
                    color = "red"
                g.edge(u, v, label = str(e), color = color)

        if (source != node):
            g.edge(source, node, label = str(d[node]), style = "dashed", color = "green")
        #g.view()
        g.attr(label=description)
        g.render(filename=os.path.join(os.path.abspath(outdir), str(img_counter)), cleanup=True)
        img_counter += 1

    # Step 1: For each node prepare the destination and predecessor
    def initialize(graph, source):
        d = {} # Stands for destination
        p = {} # Stands for predecessor
        for node in graph:
            d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
            p[node] = None
        d[source] = 0 # For the source we know how to reach
        return d, p

    def relax(node, neighbour, graph, d, p):
        # If the distance between the node and the neighbour is lower than the one I have now
        if d[neighbour] > d[node] + graph[node][neighbour]:
            hint = "Релаксация прошла успешно"
            printGraph(graph, graphType, d, node, neighbour, hint)
            # Record this lower distance
            d[neighbour]  = d[node] + graph[node][neighbour]
            p[neighbour] = node
            


    d, p = initialize(graph, source)
    hint = "Задан граф, необходимо найти путь из вершины {source} в остальные вершины графа".format(source = source)
    printGraph(graph, graphType, d, 'a', 'a', hint)


    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            for v in graph[u]: #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it

    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p


def read_data():
    inputData = []
    try:
        f = open("input.txt", "r")
        graphType = f.readline()
        graphType = graphType.rstrip("\n")
        for line in f:
            if line :
                string_list = line.split()
                inputData.append( [string_list[0], string_list[1], int(string_list[2])] )
        f.close()
    except IOError:
        print("Can not open input file")

    return graphType, inputData





#main()
graphType, data = read_data()
print(graphType)
#print(data)


graph = {}
for src, dest, length in data:
    if src not in graph:
        graph[src] = {}
    if dest not in graph:
        graph[dest] = {}
    graph[src][dest] = length

print(graph)

d, p = bellman_ford(graph, 'a', graphType)

print(d)
print(p)

#printGraph(graph, graphType)


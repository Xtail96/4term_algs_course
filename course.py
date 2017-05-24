from graphviz import Graph, Digraph

def printGraph(graph, graphType):
	if graphType == "directed":
		g = Digraph()
	else:
		g = Graph()

	for u in graph:
		for v in graph[u]: 
			g.node(u, u)
			g.node(v, v)
			g.edge(u, v, label = str(graph[u][v]))
	g.view()



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
        # Record this lower distance
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
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
		graph.update({ src : {} })
	if dest not in graph:
		graph.update({ dest : {} })
	graph[src].update({dest : length})
	
print(graph)

d, p = bellman_ford(graph, 'a')

print(d)
print(p)

printGraph(graph, graphType)


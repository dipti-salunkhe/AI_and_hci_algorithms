class Node:
	def __init__(self, f=0, g=999999, h=0, name=0):
		self.f = f
		self.g = g
		self.h = h
		self.name = name
	def setNeighbours(self, neighbours={}):
		self.neighbours = neighbours

nodes1=int(input("Enter no of nodes in the graph : "))
graph=[]
for i in range(0,nodes1):
	c=[]
	for j in range(0,nodes1):
		c.append(int(input()))
	graph.append(c)

print("\nAdjacency Matrix : ",graph,"\n")
heuristics=[]
print("Enter heuristics value of each node : ")
for k in range(nodes1):
	heuristics.append(int(input()))
print("\nHeuristics of each node is : ",heuristics,"\n\n")

a=[]
for i in range(nodes1):
	a.append(Node(h=heuristics[i], name=i))
for i in range(nodes1):
	x = []
	for j in range(nodes1):
		if(graph[i][j]!=-1):
			x.append(a[j])
		a[i].setNeighbours(x)	

startNode = a[0]
goalNode = a[nodes1-1]

def astar(start,goal):
	closedSet = set([])
	openSet = set([start])
	cameFrom = {}
	start.g = 0
	start.f = start.h
	while len(openSet)!=0:
		current = findNodeWithLowestFScore(openSet)
		if current==goal:
			return contruct_path(cameFrom, current)
		openSet.remove(current)
		closedSet.add(current)
		for neighbour in current.neighbours:
			if neighbour in closedSet:
				continue
			if neighbour not in openSet:
				openSet.add(neighbour)
			cameFrom[neighbour] = current
			
			print ("Current OpenSet: ")
			for i in openSet:
				print (i.name,end=" ")
			print("\n")
	return -1

def findNodeWithLowestFScore(openSet):
	fScore = 999999
	node = None
	for eachNode in openSet:
		if eachNode.f < fScore:
			fScore = eachNode.f
			node = eachNode
	return node

def contruct_path(cameFrom, current):
	totalPath = []
	while current in cameFrom.keys():
		current = cameFrom[current]
		totalPath.append(current)
	return totalPath

if __name__=="__main__":
	path = astar(startNode, goalNode)
	print("Path is : ", end="" )
	for node in path[::-1]:
		print(str(node.name) + "-->", end="")	
	print(goalNode.name)
	print("\nCost = " + str(goalNode.g))

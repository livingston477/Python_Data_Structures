# Add a vertex to the set of vertices and the graph
import graphlib


def add_vertex(v):
    global graph
    global vertices_no
    global vertices
    
    if v in vertices:
        print("vertex",v, "already exsits")
    else:
        vertices_no =vertices_no + 1
        vertices.append(v)
        if vertices_no > 1:  # adding culumn to the graph
            for vertex in graph:
                vertex. append(0)
        tem =[]    # adding row the graph
        for i in range(vertices_no):
            tem.append(0)
        graph.append(tem)

# Add an edgebetween vertex v1 and v2 with edge weight e
def add_edge(v1,v2,e):
    global graph  
    global vertices_no
    global vertices

    #Check if vertex v1 is a valid vertx
    if v1 not in vertices:
        print("Vertex",v1,"does not exists")
    #Check if vertex v2 is a valid vertx
    elif v2 not in vertices:
        print("vertex",v2,"does not exists")
    else:
        index1=vertices.index(v1)
        index2=vertices.index(v2)
        graph[index1][index2]=e   
        graph[index2][index1]=e   #directed and wieghted 
        
#delete node in graph
def delete_vertex(v):
    if v  not in vertices:
        print(v, "is not present in the graph")
    else:
        index1 =vertices.index(v)
        vertices_no =vertices_no - 1
        vertices.remove(v)
        graph.pop(index1)    # row deleted from graph
        for i in graph:   # deleting the column one by one  in graph
            i.pop(index1) 

# delete delete node_edge
def delete_edge(v1, v2, e):
    global graph 
    if v1 not in vertices:
        print(v1,"not present")
    elif v2 not in vertices:
        print(v2,"not present")
    else:
        index1 =vertices.index(v1)
        index2=vertices.index(v2)
        graph [index1][index2]=0
        graph [index2][index1]=0 # undirected graph
                


        
# Print the graph
def print_graph():
    global graph
    global vertices_no
    for i in range(vertices_no):
        for j in range(vertices_no):
            #if graph[i][j] !=0: 
            #print(vertices[1],"->",vertices[j],"edgw wieght:",graph[i][j])
            print(graph[i][j],end=" ")
        print()
# store the vertices in the graph
vertices=[]
# store the number ofvertices in graph
vertices_no =0
graph =[]
# Add vertices to the graph
add_vertex("A")            
add_vertex("B")
add_vertex("C")
add_vertex("D")
add_vertex("E")
add_vertex("F")

#Add the edges between the vertices along with the Weight
add_edge('A', 'B', 2)
add_edge('E', 'A', 12)
add_edge('D', 'F', 3)
add_edge('A', 'E', 4)
add_edge('B', 'C', 21)
add_edge('F', 'D', 3)

print_graph()
print("Internal representation:", graph)

        




#Adding node###
def add_node(v):
    if v in graph:
        print(v,"is already present in graph")
    else:
        graph[v]=[]

def add_edge(v1,v2, weight):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        # directed weighted graph
        list1 =[v2,weight]
        # list2 =[v1, weight]
        graph[v1].append(list1)
        # graph[v2].append(list2)

def delete_node(v):
    if v not in graph:
        print(v, "is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1= graph[i]
            #if v in list1:    #  directed  and  weighted  graph
              #  list1.remove(v)
### Undirected and unweighted graph
            for j in list1:
                if  v ==j[0]:
                    list1.remove(j)
                    break

def delete_edge(v1,v2,weight):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v1, "is not present in the graph")
    else:
        ##for weited graph undirecteed graph
        temp =[v1,weight]
        temp1 =[v2,weight]
        if temp1 in graph [v1]:
            graph[v1].remove(temp1)
            # comment for directed  and weighted graph to below line
            # graph[v2].remove(temp)
        ## for unweighted and undirected graph
        # if v2 in graph[v1]:
        #   graph[v1].remove(v2)
        #   graph[v2].remove(v1)
graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F") 

add_edge("A","B",2)
add_edge("B","F",3)
add_edge("C","D",5)
add_edge("D","B",6)
add_edge("E","F",1)
add_edge("C","A",7)
add_edge("D","A",2)

print(graph)

delete_edge("D","A",2)
# delete_node("A")
print(graph)






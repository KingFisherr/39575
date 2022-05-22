adj_list = {}
mylist = []
def add_node(node):
  if node not in mylist:
    mylist.append(node)
  else:
    print("Node ",node," already exists!")
 
def add_edge(node1, node2):
  temp = []
  if node1 in mylist and node2 in mylist:
    if node1 not in adj_list:
      temp.append(node2)
      adj_list[node1] = temp
   
    elif node1 in adj_list:
      temp.extend(adj_list[node1])
      temp.append(node2)
      adj_list[node1] = temp
       
  else:
    print("Nodes don't exist!")
 
def graph():
  for node in adj_list:
    print(node, " ---> ", [i for i in adj_list[node]])
 
#Adding nodes
add_node("html")
add_node("body")
add_node("text")
#Adding edges
add_edge("html","body")
add_edge("body","text")

#Printing the graph
graph()
 
#Printing the adjacency list
print(adj_list)

#html  --->  ['body']
#body  --->  ['text']
#{'html': ['body'], 'body': ['text']}
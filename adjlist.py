#Adjaceny list which holds nodes and edge connections along with properties for children nodes
adj_list = {}
list = []

#Add node
def add_node(node):
  if node not in list:
    list.append(node)
  else:
    print("The Node " + node + " already exists")

#Method to add edges and properties
def add_edge_property(node1, node2, property):
  flag = 0
  temp = []
  temp2 = []
  if property == "NaN":
    flag = 1
  temp2.append("Properties: " + property)

  if node1 in list and node2 in list:
    if node1 not in adj_list:
      temp.append(node2)
      if flag != 1:
        temp.append(temp2)
      adj_list[node1] = temp
   
    elif node1 in adj_list:
      temp.extend(adj_list[node1])
      temp.append(node2)
      if flag != 1:
        temp.append(temp2)
      adj_list[node1] = temp
       
  else:
    print("There are no nodes")

#Prints all values and edge connections
def printgraph():
  for node in adj_list:
    print(node, " ---> ", [i for i in adj_list[node]])
 
#Adding nodes
add_node("<html>")

add_node("<head>")
add_node("<body>")

add_node("<script>")
add_node("<title>")
add_node("<link>")

add_node("<div class = banner>")

add_node("<div class = navbar>")
add_node("<div class = content>")

add_node("function clickCounter")
add_node("text1")
add_node("css file")

add_node("<img>")
add_node("<ul>")
add_node("<h1>")
add_node("<p>")
add_node("<div>")

add_node("<li1>")
add_node("<li2>")
add_node("<li3>")
add_node("<li4>")

add_node("text2")
add_node("text3")

add_node("button1")
add_node("button2")


#Adding edges
add_edge_property("<html>","<body>","NaN")
add_edge_property("<html>","<head>","NaN")

add_edge_property("<head>","<script>","NaN")
add_edge_property("<head>","<title>","NaN")
add_edge_property("<head>","<link>","NaN")

add_edge_property("<script>","function clickCounter","NaN")
add_edge_property("<title>","text1","Sans-Serif/White")
add_edge_property("<link>","css file","CSS Extention")

add_edge_property("<body>","<div class = banner>","NaN")

add_edge_property("<div class = banner>","<div class = navbar>","NaN")
add_edge_property("<div class = banner>","<div class = content>","NaN")

add_edge_property("<div class = navbar>","<img>","logo.png")
add_edge_property("<div class = navbar>","<ul>","NaN")

add_edge_property("<ul>","<li1>","page1.html")
add_edge_property("<ul>","<li2>","page2.html")
add_edge_property("<ul>","<li3>","page3.html")
add_edge_property("<ul>","<li4>","page4.html")

add_edge_property("<div class = content>","<h1>","NaN")
add_edge_property("<div class = content>","<p>","NaN")
add_edge_property("<div class = content>","<div>","NaN")

add_edge_property("<h1>","text2","Sans-Serif/White")
add_edge_property("<p>","text3","Sans-Serif/White")

add_edge_property("<div>","button1", "HyperLink/Red")
add_edge_property("<div>","button2", "Click/Red")

#Printing the graph
printgraph()
 
#Prints the adjacency list
print(adj_list)
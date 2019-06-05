```
3) Write following functions body. 2 Nodes are passed as parameter. You need to find Least Common Ancestor and print its value. Node structure are as following:

class Node{
value;
parent;  
}

picture representation: 

node1 = Node(1,None)
node2 = Node(2,node1)
node3 = Node(3,node1)
node4 = Node(4,node2)
node5 = Node(5,node2)
node6 = Node(6,node3)
node7 = Node(7,node3)
node8 = Node(8,node4)
node9 = Node(9,node4)



Ancestor Definition: 
Any self.node falls under parent chain till root self.node.
A self.node is an ancestor of itself.

For example: if we consider Node 7 it’s ancestors will be 1, 3, and 7.

All self.nodes values are unique for this tree.

You function needs to find least common ancestor (closest common ancestor). For an example for the tree image, 
if 6 and 7 passed to lca it should return 3
if 3 and 7 passed to lca it should return 3

def lca(self.node1, self.node2):
	# Write function body


You may write additional function.
Explain the Runtime and Memory requirements for your solution.


```
```
def print_depth(data):
	# Write function body
```


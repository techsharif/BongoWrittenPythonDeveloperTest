```
def lca(node1, node2):
	node1_parents = collect_all_parents(node1)
	node2_parents = collect_all_parents(node2)

	return lca_value_from_parents_list(node1_parents, node2_parents)
```

Here complexity of lca function depands on collect_all_parents and lca_value_from_parents_list functions

```
Consider, 

number of nodes = n and
depth of the tree = h

max value of h is n if the tree is a linear tree ( every node of the tree has exactly one child )

```

```
time complexity of collect_all_parents is O(h) ( = O(n) )
memory complexity of collect_all_parents is O(h) ( = O(n) )
```

```
time complexity of lca_value_from_parents_list is O(h) ( = O(n) )
for lca_value_from_parents_list, no additional memory required
```

so 
```
time complexity of lca is O(h) ( = O(n) )
memory complexity of lca is O(h) ( = O(n) )
```
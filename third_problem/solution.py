class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

def collect_all_parents(node):
	return []

def lca_value_from_parents_list(list1, list2):
	return 0


def lca(node1, node2):
	node1_parents = collect_all_parents(node1)
	node2_parents = collect_all_parents(node2)

	return lca_value_from_parents_list(node1_parents, node2_parents)

if __name__ == '__main__':
    node1 = Node(1,None)
    node2 = Node(2,node1)
    node3 = Node(3,node1)
    node4 = Node(4,node2)
    node5 = Node(5,node2)
    node6 = Node(6,node3)
    node7 = Node(7,node3)
    node8 = Node(8,node4)
    node9 = Node(9,node4)

    print(lca(node3, node7))

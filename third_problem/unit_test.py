import unittest
from solution import *


class TestThirdProblem(unittest.TestCase):

    def setUp(self):
        self.node1 = Node(1,None)
        self.node2 = Node(2,self.node1)
        self.node3 = Node(3,self.node1)
        self.node4 = Node(4,self.node2)
        self.node5 = Node(5,self.node2)
        self.node6 = Node(6,self.node3)
        self.node7 = Node(7,self.node3)
        self.node8 = Node(8,self.node4)
        self.node9 = Node(9,self.node4)

    def test_collect_all_parents(self):
        data = [
            collect_all_parents(self.node1),
            collect_all_parents(self.node2),
            collect_all_parents(self.node3),
            collect_all_parents(self.node4),
            collect_all_parents(self.node5),
            collect_all_parents(self.node6),
            collect_all_parents(self.node7),
            collect_all_parents(self.node8),
            collect_all_parents(self.node9)

        ]

        result_data = [
            [1],
            [1, 2],
            [1, 3],
            [1, 2, 4],
            [1, 2, 5],
            [1, 3, 6],
            [1, 3, 7 ],
            [1, 2, 4, 8],
            [1, 2, 4, 9]
            
        ]

        self.assertEqual(data, result_data)


    def test_lca(self):

        data = [
            lca(self.node6, self.node7),
            lca(self.node3, self.node7),
            lca(self.node2, self.node3),
            lca(self.node9, self.node7),
            lca(self.node2, self.node6),
            lca(self.node2, self.node2),
            lca(self.node9, self.node5),
            lca(self.node5, self.node9),
            lca(self.node1, self.node1),
            lca(self.node1, self.node8),

        ]

        result_data = [3, 3, 1, 1, 1, 2, 2, 2, 1, 1]
        
        self.assertEqual(data, result_data)


if __name__ == '__main__':
    unittest.main()
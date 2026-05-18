import unittest
from proj3 import Node,heapify_up, MinHeap, insert, heapify_down

class MinHeapTest(unittest.TestCase):
    def test_heapify_up(self):
        heap = MinHeap([
            Node(2, "a"),
            Node(1, "b")
        ])
        result = heapify_up(heap, 1)
        expected = MinHeap([
            Node(1, "b"),
            Node(2, "a")
        ])
        self.assertEqual(result, expected)

    def test_insert(self):
        heap = MinHeap([
            Node(1, "a"),
            Node(2, "b")
        ])
        result = insert(heap, Node(3, "c"))
        expected = MinHeap([
            Node(1, "a"),
            Node(2, "b"),
            Node(3, "c")
        ])
        self.assertEqual(result, expected)

    def test_heapify_down(self):
        heap = MinHeap([
            Node(9, "a"),
            Node(2, "b"),
            Node(3, "c")
        ])
        result = heapify_down(heap, 0)
        expected = MinHeap([
            Node(2, "b"),
            Node(9, "a"),
            Node(3, "c")
        ])
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

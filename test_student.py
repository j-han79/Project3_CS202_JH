import unittest
from proj3 import (Node, heapify_up, MinHeap, insert, heapify_down, extract_min, count_frequency,
                   create_priority_queue, build_tree)


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

    def test_extract_min(self):
        heap = MinHeap([
            Node(2, "a"),
            Node(3, "b"),
            Node(9, "a"),
        ])
        result = extract_min(heap)
        expected = MinHeap([
            Node(3, "b"),
            Node(9, "a"),
        ]), Node(2, "a")
        self.assertEqual(result, expected)
class HuffmanTest(unittest.TestCase):
    def test_count_freq(self):
        result = count_frequency("hello")
        expected = {
            "h": 1,
            "e": 1,
            "l": 2,
            "o": 1,
        }
        self.assertEqual(result, expected)

    def test_count_empty(self):
        result = count_frequency("")
        expected = {}
        self.assertEqual(result, expected)

    def test_create_priority(self):
        frequency = {
            "a": 3,
            "b": 2,
            "c": 1
        }
        result = create_priority_queue(frequency)
        self.assertEqual(len(result.data), 3)
        self.assertEqual(result.data[0], Node(1, "c"))

    def test_build_tree(self):
        frequency = {
            "a": 3,
            "b": 2,
            "c": 1
        }
        pq = create_priority_queue(frequency)
        root = build_tree(pq)
        self.assertEqual(root.freq, 6)
        self.assertEqual(root.char, "acb")

if __name__ == '__main__':
    unittest.main()

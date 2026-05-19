import unittest
from proj3 import (Node, heapify_up, MinHeap, insert, heapify_down, extract_min, count_frequency,
                   create_priority_queue, build_tree_from_queue, generate_codes, encode, decode, huffman_encoding)


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
            "b": 1,
            "c": 2
        }
        pq = create_priority_queue(frequency)
        root = build_tree_from_queue(pq)
        self.assertEqual(root.freq, 6)
        self.assertEqual(set(root.char), {"a", "b", "c"})

    def test_generate_codes(self):
        left = Node(1, "a")
        right = Node(1, "b")
        root = Node(2, "ab", left, right)
        result = generate_codes(root)
        expected = {
            "a": "0",
            "b": "1",
        }
        self.assertEqual(result, expected)

    def test_encode(self):
        codes = {
            "a": "0",
            "b": "10",
            "c": "11"
        }
        result = encode("abc", codes)
        expected = "01011"
        self.assertEqual(result, expected)

    def test_decode(self):
        left = Node(1, "a")
        right = Node(1, "b")
        root = Node(2, "ab", left, right)
        result = decode("0110", root)
        expected = "abba"
        self.assertEqual(result, expected)

    def test_huffman_encode(self):
        encoded, decoded, codes = huffman_encoding("hello")
        self.assertEqual(decoded, "hello")
        self.assertEqual(type(encoded), str)
        self.assertEqual(type(codes), dict)

    def test_single_character_string(self):
        encoded, decoded, codes = huffman_encoding("aaaa")
        self.assertEqual(decoded, "aaaa")
        self.assertEqual(codes, {"a": "0"})
        self.assertEqual(encoded, "0000")

    def test_repeated_characters(self):
        encoded, decoded, codes = huffman_encoding("aaabbc")

        self.assertEqual(decoded, "aaabbc")
        self.assertEqual(set(codes.keys()), {"a", "b", "c"})
        self.assertEqual(type(encoded), str)

if __name__ == '__main__':
    unittest.main()

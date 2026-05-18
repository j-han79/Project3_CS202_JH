from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None  = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)

def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    new_data = heap.data[:]
    if index == 0:
        return MinHeap(new_data)
    parent = (index - 1) // 2
    if new_data[index] < new_data[parent]:
        temp = new_data[index]
        new_data[index] = new_data[parent]
        new_data[parent] = temp
        return heapify_up(MinHeap(new_data), parent)
    return MinHeap(new_data)



def insert(heap: MinHeap, element: Node) -> MinHeap:
    new_data = heap.data + [element]
    return heapify_up(MinHeap(new_data), len(new_data) - 1)


def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    new_data = heap.data[:]
    left = 2 * index + 1
    right = 2 * index + 2
    size = len(new_data)
    if left >= size:
        return MinHeap(new_data)
    smallest = left
    if right < size and new_data[right] < new_data[left]:
        smallest = right
    if new_data[smallest] < new_data[index]:
        temp = new_data[index]
        new_data[index] = new_data[smallest]
        new_data[smallest] = temp
        return heapify_down(MinHeap(new_data), smallest)

    return MinHeap(new_data)




def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    pass


        
def count_frequency(s: str)-> dict[str,int]:

    pass


def create_priority_queue(frequency: dict[str, int]) -> MinHeap:

    pass



def build_tree(priority_queue: MinHeap) -> Node:
    pass




def generate_codes(node: Node | None, prefix="", code: dict | None =None)-> dict:
    if code is None:
        code = {}  
    pass


def encode(s: str, codes: dict)-> str:
    pass


def decode(encoded_string: str, root: Node):
    pass

def huffman_encoding(s:str):
    #Do Not Change this function
    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree_from_queue(pq)
    codes = generate_codes(root)
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes


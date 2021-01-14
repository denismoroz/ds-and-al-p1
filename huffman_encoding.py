# Huffman Encoding
#
# On the first step to build frequency map of characters dictionary was used.
# That helped to do that with O(n) complexity. It requires only one time to go
# through all elements to build a frequency map.
#
# One of the main parts while building Huffman tree is to select nodes with the
# minimal frequency, for this part min heap was used. It allows to retrieve the
# minimal element with O(1) and extracting minimal element with O(logN) complexity.
#
# While building encoding map Breadth First Search to iterate over all Huffman tree
# nodes and collect encoding codes.
#
# Complexity
# Building a frequency map: O(N)
# Building a hoffman Tree: O(NlogN), for each element we have to traverse a tree and find appropriate place.
# Encoding a message: using a encoding map: O(N) where N is number of characters in input sequence.
# Decoding message: O(N) where is N is number of bits in encoded sequence.
#
import unittest
from collections import defaultdict
from heapq import heappush, heappop


class Node:
    def __init__(self, char=None, frequency=None, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.frequency == other.frequency and self.char and other.char:
            return self.char < other.char

        return self.frequency < other.frequency


class HuffmanTree:
    def __init__(self):
        self.root = None

    def get_encode_map(self):
        encode_map = {}
        self.__visit_node(self.root, "", encode_map)

        return encode_map

    def __visit_node(self, n, path, encode_map):
        if n.left:
            self.__visit_node(n.left, path + "0", encode_map)
        if n.right:
            self.__visit_node(n.right, path + "1", encode_map)

        if n.char:
            # We have reached a node with a character. So, remember path.
            encode_map[n.char] = path

    def encode(self, data):
        if data is None or len(data) == 0:
            raise ValueError("Please provide input data")

        frequencies = defaultdict(lambda: 0)
        for c in data:
            frequencies[c] += 1

        min_heap = []
        for char, frequency in frequencies.items():
            heappush(min_heap, Node(char, frequency))

        self.root = None

        while min_heap:
            left = heappop(min_heap)

            if not min_heap:
                # The last node remains in heap
                if left.left is None and left.right is None:
                    # In case if we have only one character in the message
                    self.root = Node(frequency=left.frequency, left=left)
                else:
                    self.root = left
                break

            right = heappop(min_heap)

            n = Node(frequency=left.frequency + right.frequency, left=left, right=right)
            heappush(min_heap, n)

        encode_map = self.get_encode_map()

        return "".join([encode_map[c] for c in data])

    def decode(self, data):
        result = ""
        p = None

        for c in data:
            if p is None:
                p = self.root

            if c == '0':
                p = p.left
            elif c == '1':
                p = p.right

            if p.left is None and p.right is None:
                result += p.char
                p = None

        return result


def huffman_encoding(data):
    tree = HuffmanTree()
    return tree.encode(data), tree


def huffman_decoding(data, tree):
    result = tree.decode(data)
    return result


class HuffmanTreeTestCase(unittest.TestCase):
    def test_single_character(self):
        res, tree = huffman_encoding("P")
        self.assertEqual("P", huffman_decoding(res, tree))

    def test_bigger_line(self):
        input_data = "Go! Go! Go!"
        res, tree = huffman_encoding(input_data)
        self.assertEqual(input_data, huffman_decoding(res, tree))

    def test_description_test(self):
        input_data = "AAAAAAABBBCCCCCCCDDEEEEEE"
        res, tree = huffman_encoding(input_data)
        self.assertEqual("1010101010101000100100111111111111111000000010101010101", res)
        self.assertEqual(input_data, huffman_decoding(res, tree))


if __name__ == "__main__":
    unittest.main()
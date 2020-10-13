import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    @classmethod
    def from_list(cls, _list):
        res = cls()
        for e in _list:
            res.append(e)
        return res

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        p = self.head
        res = []
        while p:
            res.append(p.value)
            p = p.next

        return res


def union(llist_1, llist_2):
    s = set(llist_1.to_list())
    s2 = set(llist_2.to_list())

    result = LinkedList()
    for e in s.union(s2):
        result.append(e)

    return result


def intersection(llist_1, llist_2):
    set1 = set(llist_1.to_list())
    set2 = set(llist_2.to_list())

    result = LinkedList()
    for e in set1.intersection(set2):
        result.append(e)

    return result


class UnionAndIntersectionTestCase(unittest.TestCase):

    def test_simple(self):
        ll1 = LinkedList.from_list([1, 2, 3])
        ll2 = LinkedList.from_list([3, 4, 5])
        self.assertEqual([1, 2, 3, 4, 5], union(ll1, ll2).to_list())
        self.assertEqual([3, ], intersection(ll1, ll2).to_list())

    def test_with_empty(self):
        ll1 = LinkedList.from_list([])
        ll2 = LinkedList.from_list([3, 4, 5])
        self.assertEqual([3, 4, 5], union(ll1, ll2).to_list())
        self.assertEqual([], intersection(ll1, ll2).to_list())

    def test_1(self):
        linked_list_1 = LinkedList.from_list([3, 2, 4, 35, 6, 65, 6, 4, 3, 21])
        linked_list_2 = LinkedList.from_list([6, 32, 4, 9, 6, 1, 11, 21, 1])

        self.assertEqual([32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21], union(linked_list_1, linked_list_2).to_list())
        self.assertEqual([4, 21, 6], intersection(linked_list_1, linked_list_2).to_list())

    def test_2(self):
        linked_list_3 = LinkedList.from_list([3, 2, 4, 35, 6, 65, 6, 4, 3, 23])
        linked_list_4 = LinkedList.from_list([1, 7, 8, 9, 11, 21, 1])

        self.assertEqual([65, 2, 35, 3, 4, 6, 1, 7, 8, 9, 11, 21, 23],
                         union(linked_list_3, linked_list_4).to_list())
        self.assertEqual([], intersection(linked_list_3, linked_list_4).to_list())


if __name__ == '__main__':
    unittest.main()
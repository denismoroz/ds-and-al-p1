import unittest
import sys


class Node(object):
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None


class LRU_Cache(object):

    def __init__(self, capacity):
        if capacity is None or capacity <= 0:
            raise ValueError("Capacity should be positive number")

        self.__capacity = capacity
        self.__data = {}
        self.__head = None
        self.__tail = None

    def get(self, key):

        if key in self.__data:
            n = self.__data[key]
            self.__move_to_tail(n)
            return n.value

        return -1

    def set(self, key, value):
        if len(self.__data) < self.__capacity:
            n = Node(key, value)
            self.__data[key] = n
            self.__add_to_tail(n)
        else:
            n = self.__delete_from_head()
            del self.__data[n.key]
            self.set(key, value)

    def __add_to_tail(self, n):
        n.next = None
        n.prev = None

        if self.__head is None:
            self.__head = n
            self.__tail = n
            return

        self.__tail.next = n
        n.prev = self.__tail
        self.__tail = n

    def __move_to_tail(self, n):
        if self.__tail == n:
            return

        if n == self.__head:
            self.__head = n.next

        if n.prev:
            n.prev.next = n.next

        if n.next:
            n.next.prev = n.prev

        self.__add_to_tail(n)

    def __delete_from_head(self):
        if self.__head is None:
            return None

        n = self.__head

        self.__head = self.__head.next
        if self.__head:
            self.__head.prev = None
        else:
            self.__tail = None

        return n

    def __repr__(self):
        elems = []
        p = self.__head
        while p:
            elems.append((p.key, p.value))
            p = p.next

        return str(elems)


class LRU_CacheTestCase(unittest.TestCase):

    def test_basic(self):
        cache = LRU_Cache(5)

        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)

        self.assertEqual(cache.get(9), -1)  # returns -1 because 9 is not present in the cache

        cache.set(5, 5)
        cache.set(6, 6)

        self.assertEqual(cache.get(3), -1)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    def test_one_element_only(self):
        cache = LRU_Cache(1)
        cache.set(1, 1)
        self.assertEqual(cache.get(1), 1)

        cache.set(2, 2)
        self.assertEqual(cache.get(1), -1)  # 1 is popped when 2 is added
        self.assertEqual(cache.get(2), 2)

    def test_without_pops(self):
        cache = LRU_Cache(10)

        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)
        cache.set(5, 5)
        cache.set(6, 6)

        for i in range(1, 7):
            self.assertEqual(cache.get(i), i)

    def test_add_none(self):
        cache = LRU_Cache(3)

        cache.set(None, None)
        self.assertEqual(cache.get(None), None)  # None is just the same element as any other

    def test_if_capacity_is_zero(self):
        with self.assertRaises(ValueError):  # Capacity is missing
            LRU_Cache(0)

    def test_if_capacity_is_None(self):
        with self.assertRaises(ValueError):  # Capacity is missing
            LRU_Cache(None)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == "tests":
        del sys.argv[1:]
        unittest.main()
    else:
        print("*" * 80)
        print("Test case 1")
        cache = LRU_Cache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        print(cache.get(1))  # 1
        print(cache.get(2))  # 2

        print(cache.get(9))  # returns -1 because 9 is not present in the cache

        cache.set(5, 5)
        cache.set(6, 6)

        print(cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

        print("*" * 80)
        print("Test case 2")

        # Single element in cache
        cache = LRU_Cache(1)
        cache.set(1, 1)
        print(cache.get(1))  # 1

        cache.set(2, 2)
        print(cache.get(1))  # -1,  1 is popped when 2 is added
        print(cache.get(2))  # 2

        print("*" * 80)
        print("Test case 3")
        # Without pops
        cache = LRU_Cache(10)

        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)
        cache.set(5, 5)
        cache.set(6, 6)

        for i in range(1, 7):
            print(cache.get(i))  # i

        print("*" * 80)
        print("Edge case 1")
        # Zero capacity
        try:
            cache = LRU_Cache(0)
        except ValueError as e:
           print(e)  # Capacity should be provided

        print("*" * 80)
        print("Edge case 2")
        # None as capacity
        try:
            cache = LRU_Cache(None)
        except ValueError as e:
            print(e)  # Capacity should be provided



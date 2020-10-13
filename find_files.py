import os
import sys
from pprint import pprint


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Queue:
    def __init__(self):
        self.tail = None
        self.head = None

    def push(self, value):
        n = Node(value)

        if self.tail is None:
            self.tail = n
            self.head = n
            return

        self.tail.next = n
        self.tail = n

    def pop(self):
        if self.head is None:
            return None

        v = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return v

    def is_empty(self):
        return self.head is None


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    queue = Queue()

    result = []

    queue.push(path)

    while not queue.is_empty():
        path = queue.pop()

        for f in os.listdir(path):
            if f in ['.', '..']:
                continue

            full_path = os.path.join(path, f)

            if os.path.isdir(full_path):
                queue.push(full_path)
            elif os.path.isfile(full_path) and full_path.endswith(suffix):
                result.append(full_path)

    return result


if __name__ == "__main__":
    pprint(find_files(sys.argv[1], sys.argv[2]))

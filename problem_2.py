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

    if path == "" or suffix == "":
        return []

    queue = Queue()

    result = []

    queue.push(path)

    while not queue.is_empty():
        path = queue.pop()

        content = []
        if os.path.isdir(path):
            content = os.listdir(path)
        else:
            content.append(path)

        for f in content:
            if f in ['.', '..']:
                continue

            full_path = os.path.join(path, f)

            if os.path.isdir(full_path):
                queue.push(full_path)
            elif os.path.isfile(full_path) and full_path.endswith(suffix):
                result.append(full_path)

    return result


if __name__ == "__main__":
    if len(sys.argv) == 2:
        pprint(find_files(sys.argv[1], sys.argv[2]))
    else:
        base = os.path.join(os.getcwd(),  "testdir")

        # Normal test case
        pprint(find_files('c', base))

        # ['./testdir/t1.c',
        #  './testdir/subdir5/a.c',
        #  './testdir/subdir1/a.c',
        #  './testdir/subdir3/subsubdir1/b.c']

        # Normal test case 2
        pprint(find_files('h', base))

        # ['./testdir/t1.h',
        #  './testdir/subdir5/a.h',
        #  './testdir/subdir1/a.h',
        #  '.testdir/subdir3/subsubdir1/b.h']

        # Normal test case 3
        pprint(find_files('l', base))

        # []

        # Edge case 1
        pprint(find_files('', base))
        # []

        # Edge case 2
        pprint(find_files('c', ''))
        # []

        # Edge case 3
        pprint(find_files('c', os.path.join(base, "t1.c")))
        # ['./testdir/t1.c', ]

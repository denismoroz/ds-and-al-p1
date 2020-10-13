import hashlib
import unittest

from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def __timestamp_to_string(self):
        return self.timestamp.strftime('%H:%M:%S%f %d/%m/%Y')

    def __str__(self):
        return "{} {} {}".format(self.__timestamp_to_string(), self.previous_hash, self.data)

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self).encode('utf-8'))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.root = None
        self.tail = None

    def add(self, data):
        b = Block(datetime.now(), data, self.tail.hash if self.tail else None)

        if self.tail:
            self.tail.next = b
            self.tail = b
        else:
            self.root = b
            self.tail = b

    def validate(self):
        p = self.root
        previous_hash = None
        while p:
            current_block_hash = p.calc_hash()
            if previous_hash is not None and previous_hash != p.previous_hash:
                return False

            previous_hash = current_block_hash
            p = p.next

        return True


class BlockchainTestCase(unittest.TestCase):
    def setUp(self):
        self.block_chain = Blockchain()

    def test_empty(self):
        self.assertTrue(self.block_chain.validate())

    def test_with_elements(self):
        self.block_chain.add("1")
        self.block_chain.add("2")
        self.block_chain.add("3")

        self.assertTrue(self.block_chain.validate())

    def test_with_corrupted_element_data(self):
        self.block_chain.add("1")
        self.block_chain.add("2")
        self.block_chain.add("3")

        # Lets corrupt second element data
        self.block_chain.root.next.data = "2.2"

        self.assertFalse(self.block_chain.validate())

        # Lets restore data but corrupt timestamp
        self.block_chain.root.next.data = "2"
        self.assertTrue(self.block_chain.validate())

        self.block_chain.root.next.timestamp = datetime.now()
        self.assertFalse(self.block_chain.validate())


if __name__ == '__main__':
    unittest.main()

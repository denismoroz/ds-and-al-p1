import unittest
import sys

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():
        return True

    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True

    return False


class IsUserInGroupTest(unittest.TestCase):
    def setUp(self):
        self.parent = Group("parent")
        self.child = Group("child")
        self.sub_child = Group("subchild")

        self.sub_child_user = "sub_child_user"
        self.sub_child.add_user(self.sub_child_user)

        self.child.add_group(self.sub_child)
        self.parent.add_group(self.child)

    def test_for_parent(self):
        self.assertTrue(is_user_in_group(self.sub_child_user, self.parent))
        self.assertFalse(is_user_in_group("parent", self.parent))
        self.assertFalse(is_user_in_group('', self.parent))

    def test_for_child(self):
        self.assertTrue(is_user_in_group(self.sub_child_user, self.child))
        self.assertFalse(is_user_in_group("dog", self.child))


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "tests":
        del sys.argv[1:]
        unittest.main()


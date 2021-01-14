# Active Directory user search
#
# To make effective solution recursive algorithm was used to iterate over all users in groups.
#
# Time and Space complexity
#
# Time depends on a active directory size in worth case there is a need to
# iterate over all groups and users, so time complexity is O(U+G) U is number of users and
# G is number of groups.
#
# Space complexity of this algorithm is proportional to maximum depth of active directory tree.
# If each function call takes O(m) space and if the maximum depth of active direcotry tree is 'n'
# then space complexity would be O(nm). Each call required to save a single stack frame.

import unittest


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

    if user is None or len(user) == 0:
        return False

    if group is None:
        return False

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
    unittest.main()


"""
To test file and folder cryptography.
"""

import unittest
import os


def make_folders_and_files():
    """
    Generates a test folder with nested files.
    :return: Boolean True or False
    """
    try:
        os.mkdir("test/")
        os.mkdir("test/testr/")
        with open("test/a.txt", "w+") as f:
            f.write("AAAAaaaa")
        with open("test/testr/b.txt", "w+") as f:
            f.write("BBBBbbbb")
        return True
    except OSError:
        return False


def delete_folders_and_files():
    """
    Folder to clean up test files.
    :return:
    """
    try:
        os.rmdir("test/")
        os.rmdir("test_encrypted/")
        return True
    except OSError:
        return False


class Crypt(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual("Hello", "Hello")


if __name__ == "__main__":
    unittest.main()

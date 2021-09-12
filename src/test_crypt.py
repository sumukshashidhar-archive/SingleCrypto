"""
To test file and folder cryptography.
"""

import unittest
import os
import os.path as path


def make_folders_and_files():
    """
    Generates a test folder with nested files.
    :return: Boolean
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
    :return: Boolean
    """
    try:
        os.rmdir("test/")
        os.rmdir("test_encrypted/")
        return True
    except OSError:
        return False


def files_exist():
    """
    Check if the created test files exist. If not, return False
    :return: Boolean
    """
    if (
        path.isdir("test/")
        and path.isdir("test/testr/")
        and path.isfile("test/a.txt")
        and path.isfile("test/testr/b.txt")
    ):
        return True
    return False


class Crypt(unittest.TestCase):
    def test_make_files(self):
        self.assertEqual(make_folders_and_files(), True)

    def test_initial_presence(self):
        self.assertEqual(files_exist(), True)

    def test_sanity(self):
        self.assertEqual("Hello", "Hello")


if __name__ == "__main__":
    unittest.main()

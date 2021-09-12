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
    print(path.curdir)
    if (
        path.isdir("test/")
        and path.isdir("test/testr/")
        and path.isfile("test/a.txt")
        and path.isfile("test/testr/b.txt")
    ):
        return True
    else:
        return False


class Crypt(unittest.TestCase):
    def test_make_files(self):
        """
        Make the test files and check if they exist.
        :return: None
        """
        self.assertEqual(make_folders_and_files(), True)
        self.assertEqual(files_exist(), True)

    def test_removed_files(self):
        """
        Remove the files and make sure that they have truly been removed.
        :return: None
        """
        self.assertEqual(files_exist(), False)

    def test_sanity(self):
        """
        Simple sanity test to check if the test cases are working as they are supposed to.
        :return: None
        """
        self.assertEqual("Hello", "Hello")


if __name__ == "__main__":
    unittest.main()

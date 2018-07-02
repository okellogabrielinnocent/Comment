from unittest import TestCase

from load_storage import Storage


class TestStorage(TestCase):

    def test_load_users(self):
        users = Storage.load_users()
        self.assertIsInstance(users, dict)

    def test_save_users(self):

        users = Storage.save_users()

import unittest
from tv_controller import TVController


class TVControllerTest(unittest.TestCase):

    def setUp(self):
        self.controller = TVController(["BBC", "Discovery", "TV1000"])

    def test_first_channel(self):
        self.assertEqual(self.controller.first_channel(), "BBC")

    def test_last_channel(self):
        self.assertEqual(self.controller.last_channel(), "TV1000")

    def test_turn_channel(self):
        self.assertEqual(self.controller.turn_channel(2), "Discovery")

    def test_next_channel(self):
        self.assertEqual(self.controller.first_channel(), "BBC")
        self.assertEqual(self.controller.next_channel(), "Discovery")
        self.assertEqual(self.controller.next_channel(), "TV1000")
        self.assertEqual(self.controller.next_channel(), "BBC")

    def test_previous_channel(self):
        self.assertEqual(self.controller.first_channel(), "BBC")
        self.assertEqual(self.controller.previous_channel(), "TV1000")
        self.assertEqual(self.controller.previous_channel(), "Discovery")
        self.assertEqual(self.controller.previous_channel(), "BBC")

    def test_current_channel(self):
        self.assertEqual(self.controller.current_channel(), "BBC")
        self.controller.next_channel()
        self.assertEqual(self.controller.current_channel(), "Discovery")

    def test_is_exist(self):
        self.assertEqual(self.controller.is_exist("BBC"), "Yes")
        self.assertEqual(self.controller.is_exist("CNN"), "No")
        self.assertEqual(self.controller.is_exist(2), "Yes")
        self.assertEqual(self.controller.is_exist(5), "No")


if __name__ == "__main__":
    unittest.main()
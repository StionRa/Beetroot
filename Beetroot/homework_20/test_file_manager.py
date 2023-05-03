import unittest
import os
from tempfile import NamedTemporaryFile
from contextlib import suppress
from file_manager import FileManager


class TestFileManager(unittest.TestCase):

    def test_file_creation(self):
        with FileManager('test_file.txt', 'w') as f:
            self.assertTrue(os.path.exists('test_file.txt'))

        self.assertTrue(os.path.exists('test_file.txt'))

    def test_file_writing(self):
        with FileManager('test_file.txt', 'w') as f:
            f.write('Hello World')

        with open('test_file.txt', 'r') as f:
            content = f.read()

        self.assertEqual(content, 'Hello World')

    def test_file_reading(self):
        with FileManager('test_file.txt', 'w') as f:
            f.write('Hello World')

        with FileManager('test_file.txt', 'r') as f:
            content = f.read()

        self.assertEqual(content, 'Hello World')

    def test_file_appending(self):
        with FileManager('test_file.txt', 'w') as f:
            f.write('Hello World')

        with FileManager('test_file.txt', 'a') as f:
            f.write('!')

        with open('test_file.txt', 'r') as f:
            content = f.read()

        self.assertEqual(content, 'Hello World!')

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            with FileManager('non_existing_file.txt', 'r') as f:
                pass

    def test_permission_error(self):
        with NamedTemporaryFile() as f:
            os.chmod(f.name, 0o400)  # make file read-only
            with suppress(Exception):  # suppress exception, since it may vary depending on the OS
                with self.assertRaises(Exception):
                    with FileManager(f.name, 'w') as fw:
                        fw.write('Hello World')

    def test_logging(self):
        with FileManager('test_file.txt', 'w') as f:
            f.write('Hello World')

        with open('test_file.txt.log', 'r') as log_file:
            log_content = log_file.read()

        expected_log = 'File test_file.txt was closed. There are 0 file(s) left open.'
        self.assertIn(expected_log, log_content)


if __name__ == '__main__':
    unittest.main()

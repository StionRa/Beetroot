import pytest
import os


@pytest.fixture
def file_obj():
    with open('test_file.txt', 'w') as f:
        f.write('Hello world!\nThis is a test.\n')

    with open('test_file.txt', 'r') as f:
        yield f

    # Clean up the test file after the fixture is used
    os.remove('test_file.txt')


def process_text_data(file_obj):
    return file_obj.read().upper()


def test_process_text_data(file_obj):
    expected_output = 'HELLO WORLD!\nTHIS IS A TEST.\n'
    assert process_text_data(file_obj) == expected_output


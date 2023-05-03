import logging


class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.counter = 0
        self.log_file = f"{file_name}.log"

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        self.counter += 1
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.counter -= 1
        logging.basicConfig(filename=self.log_file, level=logging.INFO)
        logging.info(f"File {self.file_name} was closed. There are {self.counter} file(s) left open.")
        if exc_type is not None:
            logging.error(f"An error occurred: {exc_val}")
        return False


# with FileManager('example.txt', 'w') as file:
#     file.write('hello Karolina')

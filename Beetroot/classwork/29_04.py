# # Створити контекстний менеджер для роботи з файлами:
# # як клас
# # як генератор.
# # Промоделюйте варіанти, коли ловиться виключення (в методі __exit__) і коли ні. Якщо змоделювати виникнення кількох виключень, яке ми отримаємо?
#
# # class FileManager:
# #     def __init__(self, filename, mode):
# #         self.filename = filename
# #         self.mode = mode
# #
# #     def __enter__(self):
# #         self.file = open(self.filename, self.mode)
# #         return self.file
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         self.file.close()
# #         if exc_type is not None:
# #             print(f"An exception of type {exc_type} occurred: {exc_val}")
# #         return True
# #
# # with FileManager("data.txt", "a") as file:
# #     for i in range(10000):
# #         file.write("FileManager\n")
# #         1/0
#
# from contextlib import contextmanager
#
#
# @contextmanager
# def file_manager(filename, mode='r'):
#     file = None
#     try:
#         file = open(filename, mode)
#         yield file
#     except FileNotFoundError:
#         print(f"File '{filename}' not found")
#         raise
#     except IOError:
#         print(f"Unable to open file")
#         raise
#     else:
#         try:
#             yield file
#         except Exception as e:
#             print(f"An exeption of type {type(e).__name__} occurred: {str(e)}")
#         finally:
#             if file:
#                 file.close()
#
#
# with file_manager("data.txt") as file:
#     for i in range(1000):
#         1/0
#         a = 1
#         b = "qwe"
#         c = a + b
#         print(c)
#         file.write("ascord\n")
#         print(file)
#         1/0

import time


def factorial_mult(n):
    # print(n, end=" ")
    if n == 1:
        return 1
    else:
        return n * factorial_mult(n - 1)


start_time = time.time()
print(factorial_mult(4))
end_time = time.time()


def fibonacci(n):
    # print(n, end=" ")
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


start_time_time = time.time()
print(fibonacci(4))
end_time_time = time.time()

time_taken = end_time - start_time
time_taken_taken = end_time_time - start_time_time

print("Time taken:", time_taken, "seconds")
print("Time taken:", time_taken_taken, "seconds")

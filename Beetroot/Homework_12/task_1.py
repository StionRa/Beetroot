# Write a Python program to detect the number of local variables declared in a function.
# Create scope_leer() function without variables
def scope_leer():
    pass
# Create scope() function with local variables
def scope():
    a = 5
    b = "Hello World!"
    return a, b

# Output
print("Leer function: ", scope_leer.__code__.co_nlocals, "Number of local variables available: ", scope.__code__.co_nlocals)
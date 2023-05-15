def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    l = root.pop(2)
    if len(l) > 1:
        root.insert(2, [new_branch, l, []])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_value(root):
    return root[0]


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


my_tree = binary_tree(3)
insert_left(my_tree, 5)
print(my_tree)
insert_left(my_tree, 10)
print(my_tree)
insert_right(my_tree, 4)
print(my_tree)
print(get_root_value(my_tree))
print(get_left_child(my_tree))
print(get_right_child(my_tree))
print(get_left_child(get_left_child(my_tree)))

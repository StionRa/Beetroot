def first():
    test_first = 1
    print(test_first)

    def second():
        test_second = 2
        print(test_second)

        def tree():
            test_first
            print(test_first)

        return tree()

    return second()


print(first())

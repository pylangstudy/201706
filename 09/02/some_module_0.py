def some_method(argv):
    print('some_method():', argv)


if __name__ == '__main__':
    import sys
    some_method(sys.argv)

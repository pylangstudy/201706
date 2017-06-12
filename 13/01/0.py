class MyBaseError(Exception):
    pass
class MySuperError(MyBaseError):
    pass

if __name__ == "__main__":
    raise MySuperError

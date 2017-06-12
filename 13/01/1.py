import datetime
class MyBaseError(Exception):
    pass
class MySuperError(MyBaseError):
    def __init__(self, message=None):
        self.__message = '{0:%Y-%m-%d %H:%M:%S} '.format(datetime.datetime.now()) + message
    @property
    def Message(self):
        return self.__message

if __name__ == "__main__":
    try:
        raise MySuperError('エラーメッセージですよ。')
    except MySuperError as e:
        print(e.Message)


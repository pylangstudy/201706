import datetime
class Module2Error(Exception):
    def __init__(self, message=None):
        self.__message = '{0:%Y-%m-%d %H:%M:%S} [Module2] '.format(datetime.datetime.now()) + message
    @property
    def Message(self):
        return self.__message
class SuperError(Module2Error):
    def __init__(self, message=None):
        super().__init__("[超エラー] " + message )
class SmallError(Module2Error):
    def __init__(self, message=None):
        super().__init__("[小エラー] " + message )

if __name__ == "__main__":
    try:
        raise SuperError('なんかヒドイことになった。')
    except SuperError as e:
        print(e.Message)


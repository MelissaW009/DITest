# coding:utf-8

class MyMath(object):
    @classmethod
    def isNum(cls, value):
        try:
            value + 1
        except TypeError:
            return False
        else:
            return True

    @classmethod
    def isNum2(cls, value):
        try:
            x = int(value)
        except TypeError:
            return False
        except ValueError:
            return False
        except Exception:
            return False
        else:
            return True


if __name__ == '__main__':
    a = MyMath.isNum(2.5)
    print("is a number?  ", a)

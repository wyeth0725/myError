class MyError(Exception):
    def a(self):
        print("a")
        return "errorrrrrrrrrrrrr!!!!!!!"

a = "a"
n = 1
try:
    if type(a) != type(n):
        raise MyError
except MyError as e:
    print(e.a())  
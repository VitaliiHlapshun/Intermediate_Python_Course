x = 300


def myfunc(num):
    def myinnerfunc():
        print(x)

    myinnerfunc()
    x = + num


myfunc(350)

'''
def over():
    for i in range(10):
        print("#", end = '')
    print("OVER")
    return
def into():
    print("INTO")
    return
into()
into()
into()
over()
over()
into()
over()
into()
over()
over()
print("FINISH")
'''


def gogo():
    print("GOGO")
    return


def abc():
    print("abc start")
    bts()
    gogo()
    print("abc finish")
    return


def bts():
    print("bts start")
    gogo()
    print("bts finish")
    return


gogo()
abc()
bts()
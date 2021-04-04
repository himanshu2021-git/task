import numpy


def fun():
    num = numpy.random.randint(0, 1000, size=87)
    print("Step--------1",num)

def fun2(arg = numpy.random.randint(0, 1000, size=10)):
    global dup
    dup = list(set(arg))
    print("Step--------2",dup)



def funin():
    fun()
    fun2()
    ar = numpy.array(dup)
    ad = ar +15
    even = list((ad[ad%2==0]))
    odd = list((ad[ad%2!=0]))
    print('even====',even,'\n odd====',odd)
funin()


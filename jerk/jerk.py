#coding=utf-8

#jerk.py is a simple and jerkful library
#to do some easy function more easy
'''
Jerk.py 是一个简短的python库，
它用最简陋的方式来实现一些非常小的功能
为的就是让一些经常会涉及到的功能用起来更加傻瓜，快捷
'''



#we can use "enumerate" to get both index and element
#but for an obsessive-compulsive programmer
#he need an easy function to get only the index in an easy ways
def xlen( lst, start=0, step=1 ):
    '''用xlen函数直接获得一个列表的索引'''
    return xrange( start, start+len(lst), step )



#to get the most nearest int from float
#we must use int(round( object<"float"> ))
#it is too many letters and brackets to need to be coded.
#
#int() and round() can only do with one float number
#they can't do with a list or a dic or a set()
#but xint() can do it
def xint( a ):
    '''
    用xint代替int()与round()的组合
    而且xint()可以使一个多维的数组列表、dict、set、tuple中的
    所有的float变成其最接近的整数
    不过不要传入循环dict
    '''
    
    if isinstance( a, (int, str) ):
        #a is int or str
        return a
    
    elif isinstance( a, float ):
        #a is float
        return int(round(a))
    
    elif isinstance( a, set ):
        #a is set
        return { xint(i) for i in a }

    elif isinstance( a, list ):
        #a is list
        return [ xint(i) for i in a ]

    elif isinstance( a, tuple ):
        #a is tuple
        return tuple( [ xint(i) for i in a ] )

    elif isinstance( a, dict ):
        #a is dict
        return { xint(key):xint(value) for key,value in a.iteritems() }






if __name__ == "__main__":
    
    #Have a test with xlen
    lst_test = [1,2,3,4]
    for i in xlen( lst_test ):
        print i
    print "____________"

    for i in xlen( lst_test,1 ):
        print i
    print "____________"

    for i in xlen( lst_test,1,2 ):
        print i
    print "____________"


    #have a test with xint
    a = 0.93
    print "a = {},\nxint(a)={}\n".format( a, xint (a) )
    a = [ 0.93, (291.1232332, 23.2323311) ]
    print "a = {},\nxint(a)={}\n".format( a, xint (a) )
    a = ( 0.93, 23.23, 54, [23.2, 3], '23' )
    print "a = {},\nxint(a)={}\n".format( a, xint (a) )
    a = {      0.93:239, \
          'jerk.py':(0.93, 23.2234333, 54, [23.2, 3.23323, {2.2:-0.1}]), \
               '23':-0.999 }
    print "a = {},\nxint(a)={}\n".format( a, xint (a) )

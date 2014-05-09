jerk
====

A simple python library to make python more python.
Jerkpy is a simple and jerkful library to do some easy function more easily and more jerkfully.

Now he has only four APIs, welcome to develop him together.

His mind is just to pay attention to summing up some tips from our daily coding life and make it true to be a esier using funcitonal APIs, when we are in troubles, they maybe come in handy.

Installation
====

It is recommended to use pip to install jerkpy.
<pre>
$ pip install jerk
</pre>

Another way is to download it from this git or <a href="https://pypi.python.org/pypi?name=jerk&version=0.1&:action=display">pypi</a>, and then to install it manually via <code>$ python setup.py install</code>


Get started
====

<h2>import</h2>
<b>how to import it</b>,like this below:
<pre>
from jerk import *
</pre>


References
====

<h2>xlen</h2>
<b><code>xlen( lst, start=0, step=1 )</code></b><br>
In python, we can use "enumerate" to get both index and element of a list,<br>
but for an obsessive-compulsive programmer he need an easy function to get only the index in an easy ways, which is just what "xlen" is doing.<br>
Most of this api is the function combination of "xrange()" and "len()". (The result of "xrange()" is a generator which can supply the same need in function and so that is better than "range()" of which result is a list.)<br>
[<code>lst</code>] is an argument at class of <"list"> to mean which index generator will be output;<br>
[<code>start</code>] can set the start number of the indexs. The default value of this optional argument is 0.<br>
[<code>step</code>] is an optional argument with the default value 1, which can set the step of the indexs.<br>

<b>Example:</b>
<pre>
>>> from jerk import *
>>> 
>>> lst_test = ['k','u','f','c']
>>> 
>>> for i in xlen( lst_test ):
...     print i
...
>>> 0
>>> 1
>>> 2
>>> 3
>>> 
>>> for i in xlen( lst_test,1 ):
...     print i
...
>>> 1
>>> 2
>>> 3
>>> 4
>>> 
>>> for i in xlen( lst_test,1,2 ):
...     print i
...
>>> 1
>>> 3
</pre>



<h2>xint</h2>
<b><code>xint( a )</code></b><br>
In python, if we want to get a nearest int number from a float number, we must use <code>int( round( object<"float"> ) )</code>. For coding less letters and brackets, <code>xint(a)</code> has given into birth.<br>
In addtion, if we want to make all the float numbers in a set or a dict or a list or a tuple to be transformed as int numbers, <code>int( round( object<"float"> ) )</code> can't do the job because his object input must be only one float numbers. But <code>xlen(a)</code> can do with all the things except a cyclic tree dict of course.
<br>

<b>Examples:</b>
<pre>
from jerk import *

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

>>> a = 0.93,
>>> xint(a)=1
>>> 
>>> a = [0.93, (291.1232332, 23.2323311)]
>>> xint(a)=[1, (291, 23)]
>>> 
>>> a = (0.93, 23.23, 54, [23.2, 3], '23')
>>> xint(a)=(1, 23, 54, [23, 3], '23')
>>> 
>>> a = {0.93: 239, 'jerk.py': (0.93, 23.2234333, 54, [23.2, 3.23323, {2.2: -0.1}]), '23': -0.999}
>>> xint(a)={1: 239, 'jerk.py': (1, 23, 54, [23, 3, {2: 0}]), '23': -1}
</pre>


<h2>xlist</h2>
<b><code>xlist( a )</code></b><br>
In python, if we want to get a list from a tuple, we can use <code>list()</code>. But it can not do with the elements in the tuple. So <code>xlist()</code> is recommended to use.
<br>

<b>Examples:</b>
<pre>
>>> from jerk import *
>>> 
>>> a = (0.93, (291.1232332, 23.2323311), (3,33), (3, (3, 3)), {3: 'tutorial'}, set([1, 2, 3]))
>>> print xlist(a)
>>> [0.93, [291.1232332, 23.2323311], [3, 33], [3, [3, 3]], {3: 'tutorial'}, set([1, 2, 3])]
</pre>


<h2>xtuple</h2>
<b><code>xtuple( a )</code></b><br>
In python, if we want to get a tuple from a list, we can use <code>tuple()</code>. But it can not do with the elements in the list. So <code>xtuple()</code> is recommended to use.
<br>

<b>Examples:</b>
<pre>
>>> from jerk import *
>>> 
>>> a = [0.93, [291.1232332, 23.2323311], [3, 33], [3, [3, 3]], {3: 'tutorial'}, set([1, 2, 3])]
>>> print xtuple(a)
>>>(0.93, (291.1232332, 23.2323311), (3, 33), (3, (3, 3)), {3: 'tutorial'}, set([1, 2, 3]))
</pre>


<br><br>
It only has four APIs now. Welcome to discuss which function def can make python esier and faster coding. Python is a very human language, which will be learned by every children in future.

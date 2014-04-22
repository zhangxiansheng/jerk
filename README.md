jerk
====

A simple python library to make python more python.
Jerkpy is a simple and jerkful library to do some easy function more easily and more jerkfully.

Now he has only two APIs, welcome to develop him together.

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
<b><code>xlen( lst, start=0, step=1 )</code></b>
In python, we can use "enumerate" to get both index and element of a list,
but for an obsessive-compulsive programmer he need an easy function to get only the index in an easy ways, which is just what "xlen" is doing.
Most of this api is the function combination of "xrange()" and "len()". (The result of "xrange()" is a generator which can supply the same need in function and so that is better than "range()" of which result is a list.)
[<code>lst</code>] is an argument at class of <"list"> to mean which index generator will be output;
[<code>start</code>] can set the start number of the indexs. The default value of this optional argument is 0.
[<code>step</code>] is an optional argument with the default value 1, which can set the step of the indexs.

<b>Example:</b>
<pre>
>>> from jerk import *
>>> 
>>> lst_test = [1,2,3,4]
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



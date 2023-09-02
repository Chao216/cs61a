# testing your code
## `assert`
you may use `assert` to manually test</br>
```python
assert function(arguments) == expected_results
```
## testmod
when you have made a docstring
```python
"""you will get from this runction

>>> function(arg1)
result1
>>> function(arg2)
result2
>>> function(arg3)
result3
```

you can then use testmod to test
```python
from doctest import testmod
testmod()
```
## test specified function with `run_dosctring_examples`
```python
def addone(n):
    """return value with one added

    >>> addone(1)
    2
    >>> addone(3)
    4
    >>> addone(9)
    10
    """

    return n +1


from doctest import run_docstring_examples as rde

rde(addone,globals(),True)

def cube(n):
    """return cubed value

    >>> cube(1)
    1
    >>> cube(2)
    8
    >>> cube(3)
    27
    """

    return n * n * n

rde(cube,globals(),True)
```
if you wrote many functions in one file, you can use rde to test one you need.

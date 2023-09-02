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
from doctest import run_docstring_examples as rde
rde(addone,globals(),True)
```
if you wrote many functions in one file, you can use rde to test one you need.

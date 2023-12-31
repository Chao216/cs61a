`map` with `lambda`

```python
# map(function, iterator)
list1 = list(map(lambda x: x * x, [i for i in range(1,101)]))
print(list1)
```

you will see below
```
81
6.4
this is a test
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801, 10000]
```

## explanation
`map()` takes two arguments, frist is a function, second is an iterator</br>
`lambda x: x * x` is a lambda function, `[i for i in range(1,101)]` is a list.</br>
`map` will return a map object, so we need `list()` to convert the map object to a list</br>81
```
[3, 9, 17, 27, 39, 53, 69, 87, 107, 129, 153, 179, 207, 237, 269, 303, 339, 377, 417, 459, 503, 549, 597, 647, 699, 753, 809, 867, 927, 989, 1053, 1119, 1187, 1257, 1329, 1403, 1479, 1557, 1637, 1719, 1803, 1889, 1977, 2067, 2159, 2253, 2349, 2447, 2547, 2649, 2753, 2859, 2967, 3077, 3189, 3303, 3419, 3537, 3657, 3779, 3903, 4029, 4157, 4287, 4419, 4553, 4689, 4827, 4967, 5109, 5253, 5399, 5547, 5697, 5849, 6003, 6159, 6317, 6477, 6639, 6803, 6969, 7137, 7307, 7479, 7653, 7829, 8007, 8187, 8369, 8553, 8739, 8927, 9117, 9309, 9503, 9699, 9897, 10097, 10299]
```

## currying in function
convert a function that takes multiple atgs into multiple functions that take a single arg respectively.
```python
def first(n1):
    def second(n2):
        def third(n3):
            def forth(n4):
                def fifth(n5):
                    return 3 * (n1 ** 5) + 4 * (n2 ** 4) + 5 * (n3 ** 3) + 6 * (n4 ** 2) + 7 * (n5 ** 1)
                return fifth
            return forth
        return third
    return second


res = first(1)(2)(3)(4)(5)
print(res)
```
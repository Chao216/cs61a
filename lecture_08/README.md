# review

```pyt
print(print(5))
```

| This expression   | evaluates to | interactive output |
| ----------------- | ------------ | ------------------ |
| `print(print(5))` | None         | 5<br />None        |

```py
def delay(arg):
    print("delayed!")
    def g():
        return arg
    return g
```

go check comments in **review.py** for evaluation of compound expression, as it explains better together with code
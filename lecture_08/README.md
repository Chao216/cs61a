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

```py
delay(delay)()(10)()
```

| This expression        | evaluates to | interactive output |
| ---------------------- | ------------ | ------------------ |
| `delay(delay)()`       | delay()      | delayed!           |
| `delay(delay)()(10)()` | delay(10)()  | delayed!           |
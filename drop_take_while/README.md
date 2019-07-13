# dropwhile() and takewhile() Implementation

This source code (tries to) implements in Python 3 language the methods
dropwhile() and takewhile() that
[itertools module](https://docs.python.org/3/library/itertools.html) provides.

`itertools.dropwhile(predicate, iterable)`

> Make an iterator that drops elements from the iterable as long as the
> predicate is true; afterwards, returns every element. Note, the iterator
> does not produce any output until the predicate first becomes false, so it
> may have a lengthy start-up time.

`itertools.takewhile(predicate, iterable)`

> Make an iterator that returns elements from the iterable as long as the
> predicate is true.



## How to execute

```
$ python3 test.py
```

#!/bin/python3


def dropwhile(predicate, iterable):
    for i, item in enumerate(iterable):
        if not predicate(item):
            break
    for item in iterable[i:]:
        yield(item)


def takewhile(predicate, iterable):
    for item in iterable:
        if predicate(item):
            yield(item)
        else:
            break


if __name__ == '__main__':
    pass

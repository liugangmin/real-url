from collections import deque

items = [1, 10, 20, 30, 40]


def sum(items):
    head, *tails = items
    return head + sum(tails) if tails else head


print(sum(items))



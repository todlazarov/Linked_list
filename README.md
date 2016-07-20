# [pyp-w2] Linked list

A `LinkedList` (https://en.wikipedia.org/wiki/Linked_list) is a linear data structure.
You can think of it as a re implementation of a regular Python List.

It's constructed using different Nodes. Each node has a value and a reference to the next Node in the list, as shown in the following diagram:

![linked_list](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/816px-Singly-linked-list.svg.png)

Values in the list are heterogeneous, meaning that one single `LinkedList` might contain values of many different types (ie: int, string, bools, other objects, etc).

As a regular Python `list`, it must be an ordered collection. Meaning that new Nodes in the list must be appended and iterated respecting certain order.

To create a new linked list, you just have to instantiate the `LinkedList` class, like this:

```python
>>> l = LinkedList()
```

It must also be possible to instantiate a new `LinkedList` using a pre loaded set of elements:

```python
>>> l = LinkedList([1, 5, 10])
```

Appending new elements to the list is possible by calling the `append` method:

```python
>>> l.append("hello")
>>> l.append(10)
>>> l.append("good bye")
```

To get the length of the list at certain time, call the `count` method, or just apply the `len()` built-in function to the list:

```python
>>> l.count()
3
>>> len(l)
3
```

You must also implement support to concatenate other linked lists to the current one. As in Python's `list`, there must be two possible ways of doing that, one mutating the original list:

```python
>>> l = LinkedList([1, 2, 3])
>>> l += LinkedList([8, 9, 10])
>>> len(l)
6
```

And other one not mutating it:

```python
>>> l = LinkedList([1, 2, 3])
>>> new_l = l + LinkedList([8, 9, 10])
>>> len(l)
3
>>> len(new_l)
6
```

The `pop` method must be supported to extract elements from the list.
`pop` without any parameter must return and extract the last element of the list, and `pop(n)` must do the same thing with the `nth` element in it. Example:

```python
>>> l = LinkedList([2, 4, 6, 8, 10])
>>> len(l)
5
>>> l.pop()  # return the last element
10
>>> len(l)
4
>>> l.pop(0)  # return the fist element
2
>>> len(l)
3
```

To see the String representation of a `LinkedList` at any time, you must use the `str` built-in function, or just `print` it:

```python
>>> str(l)
"[2, 4, 6, 8, 10]"
>>> print(l)
"[2, 4, 6, 8, 10]"
```

There's a last, but not less important requirement. Two `LinkedList`s containing the same elements in the same order must be considered equal:

```python
>>> LinkedList([2, 4, 6, 8]) == LinkedList([2, 4, 6, 8])
True
>>> LinkedList([2, 4, 6, 8]) == LinkedList([4, 2, 6, 8])
False
```

## Extra: coverage

Once your LinkedList is ready and your tests are passing, check to see the coverage report. It'll surely be missing a few lines, as we haven't included tests for `__getitem__` and `__ne__`. Write the missing tests to take the coverage above 95%.

## Something

# python-chess-independence-problem

started: 2020/09/17

Written in Python 3.8.5

## To run

```bash
$ python3 main.py
```

Follow on screen instructions.


## TODOs

Program could not calculate for a 6 pieces on a 9x6 board, maxed out a 4 with 32000+ combinations
To try to fix this:

The combination creator function is a bit of a mess. 

Moving over to use a single function for all pieces so I can more easily experiment with types when storing available squares.

Find a design pattern for iterating through each piece type

Finally, look for alternative approaches, and post code in forum to ask for comments and ideas.


## Questions

* Is there a performance difference in calling functions over placing the work in the code?
* How to best measure performance?
* Where to add tests?
* How to post online with calculations running client side?
  

## Notes

Membership testing with sets and dictionaries is much faster, O(1), than searching sequences, O(n). When testing "a in b", b should be a set or dictionary instead of a list or tuple.
 -but-
  Because set is an unordered collection. Since no order is expected, it makes no sense to retrieve an element at given position - it is expected to be random.

frozensets, frozensets are immutable sets. They are not faster than regular sets.

Lists are mutable and therefore cannot be used as dict keys, instead I use tuples as the dict key and a frozenset as the available values

.copy
.union
.intersection
.difference
.symettric_difference

isdisjoint
issubset
issuperset
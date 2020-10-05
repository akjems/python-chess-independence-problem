# python-chess-independence-problem

started: 2020/09/17
ended: 2020/10/05

Written in Python 3.8.5

## To run

```bash
$ python3 main.py
```

Follow on screen instructions.


## TODOs

Program sees same piece twice. See unittest_duplicate_cleaner.py as the test to pass. 

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
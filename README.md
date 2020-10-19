# python-chess-independence-problem

started: 2020/09/17
ended: 2020/10/05

Written in Python 3.8.5

## About

This program is to solve chess independence problems on M×N board for any number of Kings, Queens, Rooks, Bishops and Knights. Started as a interview prerequisite to Centrica.

"The problem is to find all distinct layouts of a set of normal chess pieces on a chess board with dimensions M×N where none of the pieces is in a position to take any of the others. 
Assume the colour of the piece does not matter, and that there are no pawns among the pieces.
Write a program which takes as input:

* The dimensions of the board: M, N.
* The number of pieces of each type (King, Queen, Bishop, Rook and Knight) to try and place on the board.

As output, the program should yield the number of distinct layouts for which all of the pieces can be placed on the board without threatening each other."

## To run

```bash
$ python3 main.py
```

Follow on screen instructions.


## Upcoming release changes

* Program sees each piece as distinct. See unittest_duplicate_cleaner.py as the test to pass.
* Only allow valid inputs
* CLI inputs instead of menu
* Estimate time of calculation before starting
* Function Outline documentation
* use classes instead


## ChangeLog

### 0.4 (2020-10-12)

* Fixes threat calculations
* Fixes combinations solver
* Updated Readme
* added unittests
* Added docstrings

### NA (2020-09-27)

* Cycles through input pieces to brute force number of combinations available

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

### Stretch Goals

* Looking into libraries and algorthimc shortcuts
* Get [chessboard](https://chessboard.readthedocs.io/en/develop/index.html) running and compare apporaches
* Host online and run on client machine
* Rewrite in JS
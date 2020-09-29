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
  


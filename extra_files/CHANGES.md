# Hello Adam!

First things first a disclaimer on my own ignorance: you can plainly see by
browsing through my own github here that I am no programming wizard. I am
actually a music teacher by day, and I've been avidly learning programming
for about the past year and the first language I learned was Python.

I was basically right in my initial comment to you where I figured that we
might be similar in skill level. In fact, I can see that you're a few steps
ahead of me in some areas, but nonetheless there are places I can see
where I can give you some advice: python idiomaticism, git, and a few things
about your online portfolio in general; not just this project.

## My Changes

I started writing a reddit reply to you, but I realized it would be easier
for me to "show you," than for me to tell you. So, that's what I've done.
In each commit, I fix a "category" of problems. One of my thoughts for your
overall project was to improve the clarity of your commit messages throughout;
more on that later, but hopefully my commit messages provide a bit of an
example.

### 1. Style

- No more than 80 characters per line.
- Delete "graveyard code"
    - Avoid committing chunks of commented code. It seems like you've already
        re-integrated that chunk in menu.py somewhere else. If you did need
        to come back to it, you could use git to return to the commit where
        you deleted it.
- Fewer blank lines
    - I think blank lines sometimes do more harm than good. Only put a blank
        line in the body of a function if you're switching to doing another
        "thing"; even then, it's probably better to define a new function
        instead.

**combination_creator.py**

- `return(variable)` becomes `return variable`.
    - No need for parenthesis
- `else: None` is unnecessary

**main.py**

- Docstring at the top doesn't need to be a `r'string'`
- `:return:` Are you saying the function returns None? I haven't seen this
    before. You can this for type annotating if you want:

>`def main() -> None:`

- Always put spaces around operators (this is endemic throughout)
    - I fixed for this file only
    - In vim, you can get most through a regexp find and replace like
    `:%s/\([\D|"]\)\([=|==|!=|\+|-|\+=]\)\([\D|"])/\1 \2 \3)/g`


- [Always surround these binary operators with a single space on either side: assignment (=), augmented assignment (+=, -= etc.), comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not), Booleans (and, or, not).](https://www.python.org/dev/peps/pep-0008/#other-recommendations)

**menu.py**

- ?? Strings on separate lines like on line 7 will be automatically concatenated,
    this is the way the python style guide recommends formatting long string
    literals.
- DONE int_input() easily avoids your input problem.
    Not sure what was meant here, so I created my own function to do this.
- Don't print input prompts longer than 80 chars. They will get wrapped in the
    terminal and look bad.

**piece_threats.py**

- For imports, always format them as follows:
    - Built-in libraries
    - newline
    - Third party pip libraries
    - newline
    - Your code
- Some people format function docstrings with the triple quotes all on one line.
    - I dislike that look, but it's a preference.
- You have a lot of trailing whitespace in your code. Your editor probably
    doesn't show it, but for people whose editors do, it looks bad.
- Again, put whitespace around all operators, even though you have a lot.

**unittest_combinations.py**

- Format long nested parenthesized / bracketed stuff like I did up to line 75.
    - There are other [acceptable styles](https://www.python.org/dev/peps/pep-0008/#indentation)
        for formatting these, and the way you've done it isn't too bad, except
        that you do have some lines that are super long.
    - Plus, by hierarchically indenting like I have, it's easier to see that
        actually, the nesting in all your methods are the same, which I could
        not immediately see at first.

### 2. Project Organization / File Structure

I haven't done this yet, but you want your python project to be exportable
as a python module, and not a random jarble of .py files all over the place.
Read
[this guide](https://docs.python-guide.org/writing/structure/)
for a good understanding of why.

So, the next thing on the adgenda is to get everything under a folder:
`chipro/`, put an `__init__.py` file in there, and move the contents of
`main.py` into `__main__.py` within that folder. That way you'll run the
project by typing `python -m chipro`, and everything will be nestled in the
`chipro` python package.

In `__init__.py`, you'll import the functions you want to be able to export
for other python scripts to import from your module. i.e.:
`from chipro import solve`

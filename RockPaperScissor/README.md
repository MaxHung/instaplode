## Project: Rock, Paper, Scissor!
Make a little game in which you play "Rock, Paper, Scissor" with your computer. 

The flow of your program should look like:
1. You enter your choice(Rock, Paper, or Scissor), while computer chooses at random.
2. Your program compares your choice to the computer's and judges who wins the game.

Your program `RockPaperScissor.py` should run like:
```Python
>>> python RockPaperScissor.py
Rock
You say Rock
Computer says Paper
Computer wins!
>>> python RockPaperScissor.py
Scissor
You say Scissor
Computer says Scissor
Tie
```
(The first line (Rock, Scissor) is not printed but what you type)

### Tips You Might Need
**How to receive information from the user?**
```Python
>>> listen = raw_input()
I type this line.
>>> print 'I heard that you said "', listen, '"'
I heard that you said "I type this line."
```
(Again, the first line (I type this line.) is not printed but what you type)

**How to generate a random number?**
```Python
>>> import random
>>> print random.randbelow(3)
2
```
`random.randbelow(n)` returns an arbitrary integer on [0,n).

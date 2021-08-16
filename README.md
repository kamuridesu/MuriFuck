# MuriFuck

A simple Brainfuck interpreter written in Python.

Usage:
Brainfuck().parser("your code here")

The tape has 30 cells and each cell can hold an unsigned int from 0 to 255. 

If you try to add 1 to the cell that currently holds a 255 value, the value of the cell turns to 0. 

If you try to subtract 1 from a cell with a 0 value, the value of the cell turns to 255.

You can also use the generator to turn any string to a valid brainfuck code.

Todo:
- The interpreter does not supports nested loops, I'll try to fix this later.

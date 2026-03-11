#!/usr/bin/env python3
"""Minesweeper game."""
import sys, random
class Minesweeper:
    def __init__(self,w=10,h=10,mines=15):
        self.w,self.h=w,h; random.seed(42)
        self.mines=set(); self.revealed=set(); self.flagged=set()
        while len(self.mines)<mines:
            self.mines.add((random.randint(0,h-1),random.randint(0,w-1)))
    def count(self,r,c):
        return sum(1 for dr in [-1,0,1] for dc in [-1,0,1]
                   if (dr or dc) and (r+dr,c+dc) in self.mines)
    def reveal(self,r,c):
        if (r,c) in self.revealed or not(0<=r<self.h and 0<=c<self.w): return
        self.revealed.add((r,c))
        if (r,c) in self.mines: return False
        if self.count(r,c)==0:
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if dr or dc: self.reveal(r+dr,c+dc)
        return True
    def display(self,show_all=False):
        for r in range(self.h):
            row=''
            for c in range(self.w):
                if show_all and (r,c) in self.mines: row+='*'
                elif (r,c) in self.revealed:
                    if (r,c) in self.mines: row+='*'
                    else:
                        n=self.count(r,c); row+=str(n) if n else '.'
                else: row+='■'
            print(f"  {row}")
g=Minesweeper()
# Auto-play: reveal safe corners
for r,c in [(0,0),(0,9),(9,0),(9,9),(5,5)]: g.reveal(r,c)
g.display()
print(f"\nRevealed: {len(g.revealed)}/{g.w*g.h-len(g.mines)} safe cells")

#!/usr/bin/env python3
"""Minesweeper game logic. Zero dependencies."""
import random, sys

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.w, self.h = width, height
        self.mines = set()
        self.revealed = set()
        self.flagged = set()
        self.game_over = False
        self.won = False
        while len(self.mines) < mines:
            self.mines.add((random.randint(0,height-1), random.randint(0,width-1)))

    def count_adjacent(self, r, c):
        count = 0
        for dr in (-1,0,1):
            for dc in (-1,0,1):
                if dr==0 and dc==0: continue
                if (r+dr, c+dc) in self.mines: count += 1
        return count

    def reveal(self, r, c):
        if self.game_over or (r,c) in self.revealed or (r,c) in self.flagged:
            return
        if (r,c) in self.mines:
            self.game_over = True; return
        self.revealed.add((r,c))
        if self.count_adjacent(r,c) == 0:
            for dr in (-1,0,1):
                for dc in (-1,0,1):
                    nr, nc = r+dr, c+dc
                    if 0<=nr<self.h and 0<=nc<self.w and (nr,nc) not in self.revealed:
                        self.reveal(nr, nc)
        if len(self.revealed) + len(self.mines) == self.w * self.h:
            self.won = True

    def flag(self, r, c):
        if (r,c) in self.revealed: return
        if (r,c) in self.flagged: self.flagged.remove((r,c))
        else: self.flagged.add((r,c))

    def display(self, show_mines=False):
        lines = ["  " + " ".join(str(i%10) for i in range(self.w))]
        for r in range(self.h):
            row = f"{r%10} "
            for c in range(self.w):
                if (r,c) in self.flagged: row += "F "
                elif (r,c) not in self.revealed and not show_mines: row += ". "
                elif (r,c) in self.mines: row += "* "
                else:
                    n = self.count_adjacent(r,c)
                    row += f"{n} " if n > 0 else "  "
            lines.append(row)
        return "\n".join(lines)

    def stats(self):
        return {"revealed": len(self.revealed), "flagged": len(self.flagged),
                "mines": len(self.mines), "remaining": self.w*self.h-len(self.revealed)-len(self.mines)}

if __name__ == "__main__":
    g = Minesweeper(10, 10, 10)
    g.reveal(5, 5)
    print(g.display())
    print(g.stats())

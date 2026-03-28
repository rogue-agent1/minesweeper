#!/usr/bin/env python3
"""Minesweeper game logic."""
import random
class Minesweeper:
    def __init__(self,rows=9,cols=9,mines=10):
        self.rows=rows;self.cols=cols;self.mines=mines
        self.board=[[0]*cols for _ in range(rows)];self.revealed=[[False]*cols for _ in range(rows)]
        self.flagged=[[False]*cols for _ in range(rows)];self.game_over=False;self.won=False
        positions=random.sample([(r,c) for r in range(rows) for c in range(cols)],mines)
        for r,c in positions: self.board[r][c]=-1
        for r in range(rows):
            for c in range(cols):
                if self.board[r][c]==-1: continue
                self.board[r][c]=sum(1 for dr in [-1,0,1] for dc in [-1,0,1] if 0<=r+dr<rows and 0<=c+dc<cols and self.board[r+dr][c+dc]==-1)
    def reveal(self,r,c):
        if self.game_over or self.revealed[r][c] or self.flagged[r][c]: return
        self.revealed[r][c]=True
        if self.board[r][c]==-1: self.game_over=True;return
        if self.board[r][c]==0:
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<self.rows and 0<=nc<self.cols: self.reveal(nr,nc)
        self._check_win()
    def flag(self,r,c): self.flagged[r][c]=not self.flagged[r][c]
    def _check_win(self):
        unrevealed=sum(1 for r in range(self.rows) for c in range(self.cols) if not self.revealed[r][c])
        if unrevealed==self.mines: self.won=True;self.game_over=True
    def display(self):
        for r in range(self.rows):
            row=""
            for c in range(self.cols):
                if self.flagged[r][c]: row+="F "
                elif not self.revealed[r][c]: row+="# "
                elif self.board[r][c]==-1: row+="* "
                elif self.board[r][c]==0: row+="  "
                else: row+=f"{self.board[r][c]} "
            print(row)
if __name__=="__main__":
    random.seed(42);g=Minesweeper(5,5,3)
    safe=[(r,c) for r in range(5) for c in range(5) if g.board[r][c]!=-1]
    g.reveal(safe[0][0],safe[0][1])
    revealed=sum(1 for r in range(5) for c in range(5) if g.revealed[r][c])
    print(f"Revealed {revealed} cells"); g.display()
    print("Minesweeper OK")

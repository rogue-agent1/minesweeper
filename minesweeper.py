#!/usr/bin/env python3
"""minesweeper - Board generator."""
import sys,argparse,json,random
def generate(w,h,mines):
    board=[[0]*w for _ in range(h)]
    positions=random.sample([(r,c) for r in range(h) for c in range(w)],mines)
    for r,c in positions:board[r][c]=-1
    for r in range(h):
        for c in range(w):
            if board[r][c]==-1:continue
            count=sum(1 for dr in(-1,0,1) for dc in(-1,0,1) if 0<=r+dr<h and 0<=c+dc<w and board[r+dr][c+dc]==-1)
            board[r][c]=count
    return board,positions
def render(b):
    return "\n".join(" ".join("*" if c==-1 else str(c) if c>0 else "." for c in row) for row in b)
def main():
    p=argparse.ArgumentParser(description="Minesweeper")
    p.add_argument("--width",type=int,default=10);p.add_argument("--height",type=int,default=10)
    p.add_argument("--mines",type=int,default=15);p.add_argument("--seed",type=int)
    p.add_argument("--json",action="store_true")
    args=p.parse_args()
    if args.seed:random.seed(args.seed)
    board,mines=generate(args.width,args.height,args.mines)
    if args.json:print(json.dumps({"width":args.width,"height":args.height,"mines":args.mines,"board":board}))
    else:print(render(board))
if __name__=="__main__":main()

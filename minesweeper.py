import argparse, random

def make_board(rows, cols, mines, seed=None):
    if seed: random.seed(seed)
    board = [[0]*cols for _ in range(rows)]
    positions = random.sample([(r,c) for r in range(rows) for c in range(cols)], mines)
    for r, c in positions: board[r][c] = -1
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == -1: continue
            count = 0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and board[nr][nc]==-1: count += 1
            board[r][c] = count
    return board

def display(board, revealed, flagged):
    rows, cols = len(board), len(board[0])
    print("   " + " ".join(f"{c:2d}" for c in range(cols)))
    for r in range(rows):
        row = f"{r:2d} "
        for c in range(cols):
            if (r,c) in flagged: row += " F"
            elif (r,c) not in revealed: row += " ■"
            elif board[r][c] == -1: row += " *"
            elif board[r][c] == 0: row += " ."
            else: row += f" {board[r][c]}"
        print(row)

def reveal(board, revealed, r, c):
    if (r,c) in revealed: return
    revealed.add((r,c))
    if board[r][c] == 0:
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                nr, nc = r+dr, c+dc
                if 0<=nr<len(board) and 0<=nc<len(board[0]):
                    reveal(board, revealed, nr, nc)

def main():
    p = argparse.ArgumentParser(description="Minesweeper")
    p.add_argument("-r", "--rows", type=int, default=9)
    p.add_argument("-c", "--cols", type=int, default=9)
    p.add_argument("-m", "--mines", type=int, default=10)
    p.add_argument("--seed", type=int)
    args = p.parse_args()
    board = make_board(args.rows, args.cols, args.mines, args.seed)
    revealed, flagged = set(), set()
    safe = args.rows * args.cols - args.mines
    while len(revealed) < safe:
        display(board, revealed, flagged)
        try: cmd = input("r/f row col: ").split()
        except EOFError: break
        if len(cmd) < 3: continue
        action, r, c = cmd[0], int(cmd[1]), int(cmd[2])
        if action == "f":
            flagged.symmetric_difference_update({(r,c)})
        elif action == "r":
            if board[r][c] == -1:
                revealed = {(r,c) for r in range(args.rows) for c in range(args.cols)}
                display(board, revealed, set())
                print("BOOM! Game over."); return
            reveal(board, revealed, r, c)
    display(board, revealed, flagged)
    print("You win!")

if __name__ == "__main__":
    main()

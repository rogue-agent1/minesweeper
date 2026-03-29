from minesweeper import Minesweeper
import random; random.seed(42)
g = Minesweeper(10, 10, 5)
assert len(g.mines) == 5
safe = None
for r in range(10):
    for c in range(10):
        if (r,c) not in g.mines:
            safe = (r,c); break
    if safe: break
g.reveal(*safe)
assert len(g.revealed) > 0
assert not g.game_over
# Flag an unrevealed non-mine cell
flag_target = None
for r2 in range(10):
    for c2 in range(10):
        if (r2,c2) not in g.revealed and (r2,c2) not in g.mines:
            flag_target = (r2,c2); break
    if flag_target: break
if flag_target:
    g.flag(*flag_target)
    assert flag_target in g.flagged
s = g.stats()
assert s["mines"] == 5
print("Minesweeper tests passed")
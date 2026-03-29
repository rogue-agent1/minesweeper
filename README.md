# minesweeper
Minesweeper game logic — reveal, flag, flood-fill, win detection.
Single-file Python, zero dependencies.
## Usage
```python
from minesweeper import Minesweeper
g = Minesweeper(10, 10, 10)
g.reveal(0, 0)
g.flag(5, 5)
print(g.display())
```

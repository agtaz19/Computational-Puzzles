# 3Blue1Brown Puzzles

Write-ups for the puzzles in this folder. Each entry gives the problem, the answer, the reasoning, and notes on the code.

---

## 1. Clock (`1-Clock.py`)

### Problem

A bug starts on the 12 of a clock. Each step, it moves to the next hour on the left or the right with equal probability. It keeps moving until every hour has been visited. What is the probability that 6 is the last hour visited?

### Answer

$$P(\text{6 is last}) = \frac{1}{11} \approx 9.09\%$$

The surprising part is that this holds for every hour other than 12. The hours next to the start (1 and 11) are just as likely to be last as the hour directly across (6).

### Reasoning

Label the hours $0, 1, \dots, 11$ with the bug starting at $0$. For hour $k$ to be last, two things must happen in order:

1. The bug reaches one neighbor of $k$ (either $k-1$ or $k+1$) without ever touching $k$.
2. From that neighbor, the bug walks all the way around the other side of the clock to the other neighbor, again without touching $k$.

Step 2 is a gambler's ruin problem. Standing at $k-1$, the bug is 1 step from $k$ and 10 steps (the long way) from $k+1$. For a fair random walk, the probability of reaching the far end before the near end is

$$\frac{1}{1 + 10} = \frac{1}{11}.$$

The same is true starting from $k+1$. Since step 1 must end at one of the two neighbors, and step 2 has probability $\tfrac{1}{11}$ either way,

$$P(k \text{ is last}) = P(\text{reach a neighbor first}) \cdot \frac{1}{11} = 1 \cdot \frac{1}{11} = \frac{1}{11}.$$

The answer does not depend on $k$, so all 11 hours are equally likely.

### Code notes

The script runs one million random walks and counts which hour each walk ends on. Every hour from 1 to 11 should come out near $9.09\%$, and hour 0 (the 12) should be $0\%$.

Two points if the script is revisited:

- The `print` inside the loop runs one million times and is the main cost. Removing it makes the script much faster.
- Hour `0` in the output is the 12 on the clock.

---

## 2. Grid Bacteria (`2-GridBacteria.py`)

### Problem

A single cell sits at the origin $(0, 0)$ of the first-quadrant grid. In one move, a cell at $(x, y)$ can split into two cells at $(x+1, y)$ and $(x, y+1)$, and the original cell dies. A move is only allowed if both target spots are empty, since each point can hold at most one cell.

What is the minimum number of moves needed to clear the $3 \times 3$ box in the corner, meaning no cells remain at any point $(x, y)$ with $0 \le x, y \le 2$?

### Answer

It cannot be done. No finite number of moves clears the box.

This is a well-known result, often called Kontsevich's chip problem. A stronger version holds: even the three corner cells $(0,0)$, $(1,0)$, $(0,1)$ can never be cleared at the same time.

### Reasoning

Give each point a weight:

$$w(x, y) = 2^{-(x+y)}.$$

**The total weight never changes.** A cell at $(x, y)$ has weight $2^{-(x+y)}$. It is replaced by two cells, each with weight $2^{-(x+y+1)}$, which add up to the same amount. The process starts with one cell of weight $1$, so the total weight of all cells is always $1$.

**The whole grid has weight 4.**

$$\sum_{x \ge 0} \sum_{y \ge 0} 2^{-(x+y)} = \left(\sum_{x \ge 0} 2^{-x}\right)^2 = 2^2 = 4.$$

**The box has weight $\tfrac{49}{16}$.**

$$\left(1 + \tfrac{1}{2} + \tfrac{1}{4}\right)^2 = \left(\tfrac{7}{4}\right)^2 = \tfrac{49}{16}.$$

**Everything outside the box has weight $\tfrac{15}{16}$.**

$$4 - \tfrac{49}{16} = \tfrac{15}{16} < 1.$$

If the box were empty, every cell would sit outside it. After a finite number of moves there are finitely many cells, one per point at most, so their total weight would be strictly less than $\tfrac{15}{16}$. That contradicts the total always being $1$. So the box can never be cleared.

### Code notes

The file currently holds only the problem statement. A natural next step is a search over move sequences that shows the cells piling up against the edge of the box, which illustrates why the weight argument has to be true.

The docstring lists the corners as $(0,0)$ through $(3,3)$, which would be a $4 \times 4$ set of points. The answer is the same under either reading, since a larger box is even harder to clear.

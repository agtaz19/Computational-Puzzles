# 1. The Ladybug Clock Puzzle: Solution

**Monthly Mindbenders, January 2026** · Code: [`1-Clock.py`](1-Clock.py) · [Back to the puzzle list](README.md)

## Problem

A ladybug starts on the 12 of a clock. Every time the clock strikes, she moves to one of the two neighboring numbers, each with probability $\tfrac{1}{2}$. She keeps going until she has visited every number at least once. What is the probability that 6 is the last new number she visits?

## Answer

$$P(\text{6 is last}) = \frac{1}{11} \approx 9.09\%$$

The same holds for every hour other than 12. The hours next to the start (1 and 11) are just as likely to be last as the hour directly across (6).

## Reasoning

Label the hours $0, 1, \dots, 11$ with the ladybug starting at $0$. For hour $k$ to be last, two things must happen in order:

1. She reaches one neighbor of $k$ (either $k-1$ or $k+1$) without touching $k$.
2. From that neighbor, she walks all the way around the other side of the clock to the other neighbor, again without touching $k$.

Step 1 is certain to happen. The walk eventually visits every hour, and before it first lands on $k$ it must land on one of the neighbors of $k$.

Step 2 is a gambler's ruin problem. Standing at $k-1$, she is 1 step from $k$ and 10 steps (the long way around) from $k+1$. For a fair random walk started between two barriers at distances $a$ and $b$, the probability of reaching the barrier at distance $b$ first is $\tfrac{a}{a+b}$. Here $a = 1$ and $b = 10$, so

$$P(\text{reach } k+1 \text{ before } k) = \frac{1}{1 + 10} = \frac{1}{11}.$$

The same calculation holds starting from $k+1$. Combining the two steps,

$$P(k \text{ is last}) = \underbrace{P(\text{step 1})}_{=\,1} \cdot \frac{1}{11} = \frac{1}{11}.$$

The result does not depend on $k$, so all 11 hours are equally likely to be last.

## Computational check

`1-Clock.py` simulates one million walks and counts which hour each one ends on. Every hour from 1 to 11 comes out near $9.09\%$, and hour 0 (the 12) is never last.

The script prints a line for every simulation, which is most of its run time. Removing that `print` makes it much faster. Hour `0` in the output corresponds to the 12 on the clock.

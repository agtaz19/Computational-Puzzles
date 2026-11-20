"""
What's the Perfect Encoding? How Do You Know?
3Blue1Brown Short (not part of the Monthly Mindbenders series)
Released: 2026-06-10
Video: https://www.youtube.com/shorts/7L_eTem1SQ4
Full video: https://youtu.be/l6DKRf-fAAM (Compression is Intelligence, Part 1)

The problem:
A robot on a distant moon receives movement instructions from Earth. Each
instruction is one of four steps: up, down, left, or right. The robot follows
a biased random walk: half of its moves are up, a quarter are down, an eighth
are left, and an eighth are right.

Part 1: Find the most efficient way to encode these instructions in binary,
meaning the fewest bits per instruction on average.

Part 2 (challenge): Prove that your encoding is optimal, so that no other
encoding can do better.
"""

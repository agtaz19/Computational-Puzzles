# Computational-Puzzles

A collection of math and probability puzzles worked through with code.

## Why this repo exists

Many puzzles have a short, clever answer that is easy to state and hard to trust. This repo is a place to check those answers by simulation or brute force, then write down the argument that explains the result. It also serves as practice for the kind of problems asked in quantitative finance interviews.

## Structure

```
Computational-Puzzles/
├── README.md              This file
├── LICENSE                MIT License
├── 3Brown1Blue/           Puzzles from 3Blue1Brown
│   ├── README.md          Write-up of each problem
│   ├── 1-Clock.py         Random walk on a clock: which hour is visited last?
│   └── 2-GridBacteria.py  Cell replication on a grid: can a corner box be cleared?
└── JaneStreet/            Puzzles from Jane Street (monthly puzzles)
    └── README.md          Write-up of each problem
```

Each folder holds one source of puzzles. Files are numbered in the order they were added, using the pattern `N-ShortName.py`. The `README.md` in each folder states each problem, gives the answer, and explains the reasoning.

## Running the code

The scripts use only the Python standard library.

```bash
python3 3Brown1Blue/1-Clock.py
```

# Computational-Puzzles

A collection of math and probability puzzles worked through with code.

## Why this repo exists

Many puzzles have a short, clever answer that is easy to state and hard to trust. This repo is a place to check those answers by simulation or brute force, then write down the argument that explains the result. It also serves as practice for the kind of problems asked in quantitative finance interviews.

## Sources

- **[Monthly Mindbenders](https://momath.org/mindbenders/)**: a monthly puzzle series from the National Museum of Mathematics (MoMath), curated by Peter Winkler and presented on YouTube by 3Blue1Brown. These live in `3Brown1Blue/`.
- **Jane Street puzzles**: Jane Street's monthly puzzle series. These live in `JaneStreet/`.

## Structure

```
Computational-Puzzles/
├── README.md                       This file
├── LICENSE                         MIT License
├── 3Brown1Blue/                    3Blue1Brown x MoMath Monthly Mindbenders
│   ├── README.md                   Questions, release dates, and spoiler answers
│   ├── 1-Clock.py                  Jan 2026: Ladybug clock
│   ├── 1-Clock_Solution.md         Technical write-up for puzzle 1
│   ├── 2-GridBacteria.py           Feb 2026: Lattice bacteria
│   ├── 3-SubsetSum.py              Mar 2026: Subset sum
│   ├── 4-CoveringPoints.py         Apr 2026: Covering 10 points
│   ├── 5-YarnLoops.py              May 2026: Yarn loops
│   ├── 6-RandomChords.py           Jun 2026: 100 random chords
│   ├── 7-SugarCubes.py             Jul 2026: 64 sugar cubes
│   ├── 8-JumpingPegs.py            Aug 2026: Jumping pegs
│   ├── 9-PhoneNumber.py            Sep 2026: Phone number
│   ├── 10-SphereIntersection.py    Oct 2026: Sphere intersection
│   └── Extras/                     3Blue1Brown puzzles outside the monthly series
│       ├── README.md
│       └── 1-PerfectEncoding.py    Optimal binary encoding of a biased walk
└── JaneStreet/                     Jane Street monthly puzzles
    └── README.md
```

## Conventions

- Files are numbered in release order: `N-ShortName.py`.
- Each folder's `README.md` lists every puzzle with its question and release date. The answer sits behind a spoiler tag.
- Full technical solutions go in a separate file, `N-ShortName_Solution.md`, linked from the folder README.
- A code file that holds only a docstring is a puzzle that has been added but not yet solved.

## Running the code

The scripts use only the Python standard library.

```bash
python3 3Brown1Blue/1-Clock.py
```

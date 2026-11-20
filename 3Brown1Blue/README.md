# 3Blue1Brown × MoMath Monthly Mindbenders

Puzzles from the [Monthly Mindbenders](https://momath.org/mindbenders/) series, curated by Peter Winkler for the National Museum of Mathematics (MoMath) and presented on YouTube by Grant Sanderson (3Blue1Brown). A new puzzle comes out each month.

Each entry below gives the question and the answer, hidden behind a spoiler. Full technical solutions are in separate write-up files, linked from each entry when available.

| # | Puzzle | Month | Released | Code | Write-up |
|---|---|---|---|---|---|
| 1 | Ladybug Clock | Jan 2026 | 2026-01-16 | [`1-Clock.py`](1-Clock.py) | [Solution](1-Clock_Solution.md) |
| 2 | Lattice Bacteria | Feb 2026 | 2026-02-18 | [`2-GridBacteria.py`](2-GridBacteria.py) | |
| 3 | Subset Sum | Mar 2026 | 2026-03-25 | [`3-SubsetSum.py`](3-SubsetSum.py) | |
| 4 | Covering 10 Points | Apr 2026 | 2026-04-16 | [`4-CoveringPoints.py`](4-CoveringPoints.py) | |
| 5 | Yarn Loops | May 2026 | 2026-05-21 | [`5-YarnLoops.py`](5-YarnLoops.py) | |
| 6 | 100 Random Chords | Jun 2026 | 2026-06-16 | [`6-RandomChords.py`](6-RandomChords.py) | |
| 7 | 64 Sugar Cubes | Jul 2026 | 2026-07-24 | [`7-SugarCubes.py`](7-SugarCubes.py) | |
| 8 | Jumping Pegs | Aug 2026 | 2026-08-18 | [`8-JumpingPegs.py`](8-JumpingPegs.py) | |
| 9 | Phone Number | Sep 2026 | 2026-09-25 | [`9-PhoneNumber.py`](9-PhoneNumber.py) | |
| 10 | Sphere Intersection | Oct 2026 | 2026-10-25 | [`10-SphereIntersection.py`](10-SphereIntersection.py) | |

"Released" is the date the puzzle's video went up on YouTube. Puzzles that are not part of the monthly series are in [`Extras/`](Extras/).

---

## 1. Ladybug Clock

**Released:** 2026-01-16 · [Video](https://www.youtube.com/shorts/t3jZ2xGOvYg) · Code: [`1-Clock.py`](1-Clock.py)

A ladybug starts on the 12 of a clock. Each time the clock strikes, she moves to a neighboring number, left or right with equal probability. She continues until she has visited every number. What is the probability that 6 is the last new number she visits?

<details>
<summary>Answer (spoiler)</summary>

$\tfrac{1}{11} \approx 9.09\%$. The simulation gives the same value for every hour except 12.

</details>

Full solution: [1-Clock_Solution.md](1-Clock_Solution.md)

---

## 2. Lattice Bacteria

**Released:** 2026-02-18 · [Video](https://www.youtube.com/shorts/d0ai33oqqDE) · Code: [`2-GridBacteria.py`](2-GridBacteria.py)

A single bacterium starts at the origin of the grid. A bacterium at $(x, y)$ can divide, dying and leaving new bacteria at $(x+1, y)$ and $(x, y+1)$, but only if both of those points are empty. Roughly how many divisions does it take to clear every bacterium out of the box with corners $(0,0)$, $(3,0)$, $(0,3)$, $(3,3)$?

<details>
<summary>Answer (spoiler)</summary>

It cannot be done. No finite number of divisions clears the box.

</details>

---

## 3. Subset Sum

**Released:** 2026-03-25 · [Video](https://www.youtube.com/shorts/4h5BEALuh44) · Code: [`3-SubsetSum.py`](3-SubsetSum.py)

A friend picks 10 different whole numbers between 1 and 100. You try to find two non-overlapping, nonempty groups of her numbers with the same sum. With best play, who wins?

---

## 4. Covering 10 Points

**Released:** 2026-04-16 · [Video](https://www.youtube.com/shorts/QLu_ZsRc_G0) · Code: [`4-CoveringPoints.py`](4-CoveringPoints.py)

An opponent places 10 points anywhere on the plane. You must cover all of them with unit disks that do not overlap. Can you always do it?

---

## 5. Yarn Loops

**Released:** 2026-05-21 · [Video](https://www.youtube.com/shorts/ZHXt0-_gSj4) · Code: [`5-YarnLoops.py`](5-YarnLoops.py)

A box holds 50 pieces of string. Repeatedly grab two loose ends at random and tie them together until no loose ends remain. On average, how many loops do you end up with?

---

## 6. 100 Random Chords

**Released:** 2026-06-16 · [Video](https://www.youtube.com/shorts/wGffBCfrAsE) · Code: [`6-RandomChords.py`](6-RandomChords.py)

Draw 100 chords of a circle, each by joining two points chosen uniformly at random on the circle. What is the expected number of intersection points?

---

## 7. 64 Sugar Cubes

**Released:** 2026-07-24 · [Video](https://www.youtube.com/shorts/6XPlmCDNLNc) · Code: [`7-SugarCubes.py`](7-SugarCubes.py)

64 sugar cubes form a 4×4×4 block, and each cube is white, blue, or brown. Prove that you can always find 12 cubes of one color that split into 6 pairs, with the same distance between centers in every pair.

The MoMath sheet for July poses a different puzzle (six dice), noted in the code file.

---

## 8. Jumping Pegs

**Released:** 2026-08-18 · [Video](https://www.youtube.com/shorts/rYyJm1tD3d0) · Code: [`8-JumpingPegs.py`](8-JumpingPegs.py)

Pegs sit on three corners of a square. A move jumps one peg over another, landing the same distance away on the far side; the jumped peg stays put. Can a peg ever reach the fourth corner?

---

## 9. Phone Number

**Released:** 2026-09-25 · [Video](https://www.youtube.com/shorts/ausLKMojXaY) · Code: [`9-PhoneNumber.py`](9-PhoneNumber.py)

If your 10-digit phone number ends in 1, 3, 7, or 9, prove that some multiple of it is written using only the digit 1.

---

## 10. Sphere Intersection

**Released:** 2026-10-25 · [Video](https://www.youtube.com/shorts/V_uq3v6xK-4) · Code: [`10-SphereIntersection.py`](10-SphereIntersection.py)

Two unit balls are placed at random, given that they overlap. What is the expected volume of their intersection?

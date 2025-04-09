# Stable Matching Algorithm Explanation

## Overview
The **Stable Matching Problem** is a fundamental problem in combinatorial optimization that seeks to find a **stable** matching between two equal-sized sets of participants (e.g., men and women in a marriage problem, medical students and hospitals in a residency matching program). A matching is considered **stable** if there are no two participants who would rather be with each other than with their current partners.

This implementation follows the **Gale-Shapley algorithm** (also known as the **Deferred Acceptance Algorithm**) to solve the problem efficiently.

---

## Problem Statement
Given **N men** and **N women**, each participant ranks all members of the opposite group in order of preference. The goal is to determine a stable matching based on these preferences.

### Input Format
1. **First Line**: An integer **N** (1 ≤ N ≤ 100), specifying the number of men and women, followed by a character (**m** or **w**) indicating whether men (**m**) or women (**w**) make the proposals first.
2. **Next N Lines**: Each line contains the name of a man, followed by his preference list (ordered from most to least preferred partner).
3. **Next N Lines**: Each line contains the name of a woman, followed by her preference list (ordered from most to least preferred partner).

### Output Format
- The program prints **N pairs** (one per line), where each pair represents a man and the woman he is matched with. The output should preserve the input order of the men.

---

## Algorithm Explanation
The algorithm follows these steps:

### **1. Initialization**
- Two dictionaries store the preference lists:
  - `men_prefs`: Stores each man's ranked list of women.
  - `women_prefs`: Stores each woman’s ranked list of men.
- A dictionary `engaged` keeps track of current pairings.
- A dictionary `proposals` tracks the index of the next proposal each man (or woman) will make.
- A set `free_men` (or `free_women` if women propose first) tracks the unmatched participants.

### **2. Proposal Phase**
- While there are free proposers (men or women depending on the input):
  - The proposer chooses the next person from their preference list (in order).
  - If the chosen person is **not engaged**, they accept the proposal and form a pair.
  - If the chosen person **is engaged**:
    - They compare their current partner with the new proposer.
    - If they prefer the new proposer, they **break up** and engage with the new proposer.
    - Otherwise, they **reject** the new proposer, who remains free.

### **3. Matching Completion**
- This continues until all participants are matched, at which point the algorithm terminates with a stable matching.

---

## Complexity Analysis
- Each proposer makes at most **N proposals** (since they propose sequentially through their list).
- Each participant considers at most **N proposals**.
- The worst-case complexity is **O(N²)**, which is efficient for reasonable values of N (≤ 100).

---

## Example Walkthrough
### **Input:**
```
3 m
Xavier Amy Bertha Clare
Yancey Bertha Amy Clare
Zeus Amy Bertha Clare
Amy Yancey Xavier Zeus
Bertha Xavier Yancey Zeus
Clare Xavier Yancey Zeus
```

### **Processing:**
1. Xavier proposes to Amy → Amy accepts.
2. Yancey proposes to Bertha → Bertha accepts.
3. Zeus proposes to Amy, but Amy prefers Xavier → Zeus stays free.
4. Zeus proposes to Bertha, but Bertha prefers Yancey → Zeus stays free.
5. Zeus proposes to Clare → Clare accepts.

### **Output:**
```
Xavier Amy
Yancey Bertha
Zeus Clare
```

---

## Edge Cases Considered
- **Smallest Input (N=1)**: Works correctly with a single pair.
- **Worst-Case Scenario (N=100)**: Runs in O(N²) time and remains computationally feasible.
- **Already Stable Matching**: If the input already provides a stable matching, it remains unchanged.
- **Reverse Preferences**: The algorithm correctly adjusts even if each group prefers the least preferred partner first.

---

## Conclusion
The **Gale-Shapley algorithm**(also called the *Deferred Acceptance Algorithm*) efficiently finds a stable matching in **O(N²) time complexity**. This implementation ensures:
- Correct handling of input format.
- Proper validation of preference lists.
- Efficient execution within the problem constraints.
- Stability of the resulting matches.



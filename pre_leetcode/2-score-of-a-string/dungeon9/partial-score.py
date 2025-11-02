# # Dungeon 9 — Partial Score Tracker 🏹
#
# **Goal:** Practice summing absolute differences between adjacent characters in a string,
#         but only for the first half of the string.
#
# ## Tasks:
# 1. Ask the user to enter a string (at least 2 characters long).
# 2. Determine the halfway point of the string (integer division if length is odd).
# 3. Initialize a variable `partial_score` to 0.
# 4. Loop through the string **by index** from the first character to the character just before the halfway point.
# 5. For each pair of adjacent characters:
#    - Convert both characters to ASCII using `ord()`.
#    - Compute the **absolute difference** using `abs()`.
#    - Add the difference to `partial_score`.
# 6. After the loop, print the partial score.
#
# ### Example (concept only):
# Input: "hello"
# - Halfway index: 2
# - 'h' = 104, 'e' = 101 → difference = 3
# - 'e' = 101, 'l' = 108 → difference = 7
# Partial score = 3 + 7 = 10
#
# **Purpose:** Prepares you for the full Score of a String problem on LeetCode by practicing
# summing differences in a smaller section of the string.

# Write your code below:



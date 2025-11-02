# # Dungeon 7 — Difference List Builder 🧩

# **Goal:** Store each adjacent ASCII difference into a list.

# ## Tasks:
# 1. Ask the user to enter a string (at least 2 characters long).
# 2. Create an empty list called `differences`.
# 3. Loop through the string **by index** from the first character to the second-to-last character.
# 4. For each pair of adjacent characters:
#    - Convert both characters to ASCII with `ord()`.
#    - Compute the **absolute difference** using `abs()`.
#    - Append the difference to the `differences` list.
# 5. After the loop, print the `differences` list.

# ### Example (concept only):
# Input: `"abc"`
# Differences: `[1, 1]`  
# Because:
# - |97 - 98| = 1  
# - |98 - 99| = 1

# **Purpose:** This prepares you for building the final **total score** list used in Score of a String on LeetCode.


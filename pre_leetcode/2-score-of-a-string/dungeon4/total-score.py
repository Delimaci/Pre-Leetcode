# # Dungeon 4 — Total Score Tracker 🏹
# **Goal:** Start calculating the total score of a string by summing absolute differences between adjacent characters.

# ## Tasks:
# 1. Ask the user to enter a string (at least 2 characters long).
# 2. Initialize a variable `total_score` to 0.
# 3. Loop through the string **by index** from the first character to the second-to-last character.
# 4. For each pair of adjacent characters:
#    - Get their ASCII values using `ord()`.
#    - Compute the **absolute difference** using `abs()`.
#    - Add the difference to `total_score`.
# 5. After the loop, print the total score.

# ### Example (concept, not code):
# Input: "hi"
# - 'h' = 104, 'i' = 105 → difference = 1
# Total score = 1

# **Purpose:** This prepares you for the full "Score of a String" problem on LeetCode.

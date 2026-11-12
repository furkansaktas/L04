# Bug reports for exercise2.py

Line: 3
Problem: The function `is_passing` should return `True` if the grade is 5 or more, but it uses `>` instead of `>=`, which means grades exactly equal to 5 will be incorrectly classified as failing.
Example: is_passing(5) should return True, but currently returns False.
Fix: return grade >= 5

Line: 8
Problem: The function `is_valid_password` requires at least 8 characters, but it uses `> 8` which means passwords with exactly 8 characters are rejected. The requirement is "at least 8", which includes 8.
Example: is_valid_password("abcdefgh") should return True, but currently returns False.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: The `clamp` function has a logical error in its implementation. It uses `max(low, min(x, low))`, which simplifies to `low` regardless of x, because `min(x, low)` will always be at most `low`, and then `max(low, ...)` will always return `low`. This means the function always returns `low`, regardless of the input x.
Example: clamp(10, 1, 5) should return 5, but currently returns 1.
Fix: return max(low, min(x, high))

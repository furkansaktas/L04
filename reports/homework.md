# Bug reports for homework.py

Line: 2
Problem: The formula in the docstring is incorrect. It states "F = C * 9+5 + 32", which is mathematically wrong. The correct formula is F = (C * 9/5) + 32. The current implementation computes c * 5 + 9 + 32, which is not equivalent to the proper conversion.
Example: celsius_to_fahrenheit(0) → returns 37, but should return 32 (correct Fahrenheit for 0°C)
Fix: return c * 9/5 + 32

Line: 8
Problem: The condition "if score > 90" is incorrect according to the docstring, which specifies "A for 90 or more". The condition should use >= instead of > to include 90.
Example: get_grade(90) → returns "F", but should return "A"
Fix: if score >= 90:

Line: 21
Problem: The variable `best` is initialized to 0, which is incorrect when the list may contain negative numbers. If all numbers are negative, the function will incorrectly return 0 (the initial value) instead of the largest number. The initialization should be to the first element of the list.
Example: find_max([-5, -10, -3]) → returns 0, but should return -3
Fix: best = numbers[0]

Line: 31
Problem: The leap year logic is incorrect. The condition "year % 4 == 0 and year % 100 != 0" fails for years divisible by 400 (like 2000). According to the docstring, years divisible by 100 are not leap years unless also divisible by 400. The correct condition is: divisible by 4, and if divisible by 100, then also divisible by 400.
Example: is_leap_year(1900) → returns False (correct), but is_leap_year(2000) → returns False (incorrect, should be True)
Fix: return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

Line: 37
Problem: The while loop condition uses `low < high`, which causes the loop to terminate when low == high. This means the loop will not check the last element when the list has only one element. In a list of length 1, low and high are equal at the start, so the loop body is skipped entirely, and the function returns -1 when the target is present, which is incorrect.
Example: binary_search([5], 5) → returns -1, but should return 0
Fix: while low <= high:

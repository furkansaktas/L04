# Bug reports for exercise1.py

Line: 3
Problem: The docstring is incorrect because it states "true for even numbers" which is misleading. The function correctly returns True for even numbers, but the docstring does not clearly state that it returns a boolean value or that it evaluates whether a number is even. This could lead to confusion about the function's output type and behavior.
Example: is_even(4)  # Expected: True, but docstring suggests it's just "true for even numbers" without clarifying it's a boolean
Fix: """Returns True if the number is even, False otherwise."""

Line: 12
Problem: The docstring "twice the number n" is vague and does not clearly describe the function's behavior or output. It should explicitly state that it returns the number multiplied by two, which improves clarity and usability.
Example: double(5)  # Expected: 10, but docstring does not clearly indicate the output
Fix: """Returns the number multiplied by two."""

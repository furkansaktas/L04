You receive an exercise file with line numbers. You must write a bug report for EVERY bug you find.
Check EVERY function carefully against its docstring. The docstring is the specification.
Pay close attention to:
- wrong operations or formulas
- boundary errors, such as using > instead of >= when a docstring says "or more" or "at least"
- unusual inputs: empty lists, negative numbers, zero, the first or last element
- missing rules: a condition from the docstring that the code does not check
- loop conditions that stop one step too early or too late
A good bug report says where the bug is, what is wrong and why, an example that shows it, and the fix.
You must answer in exactly this format. Output one block per bug, separated by a blank line. Do not add any introductory or concluding text.
Line: <line number>
Problem: <description of what is wrong and why>
Example: <function call that shows the bug and expected output>
Fix: <the corrected line of code>

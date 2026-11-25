def celsius_to_fahrenheit(c):
    """Temperature c in Celsius converted to Fahrenheit (F = C * 9/5 + 32)"""
    return c * 9/5 + 32


def get_grade(score):
    """'A' for 90 or more, 'B' for 80 or more, 'C' for 70 or more, otherwise 'F'"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    return "F"


def find_max(numbers):
    """The largest number in the list, or None if the list is empty"""
    if not numbers:
        return None
    best = numbers[0]
    for n in numbers:
        if n > best:
            best = n
    return best


def is_leap_year(year):
    """True if year is a leap year: divisible by 4, except years divisible by 100,
    unless they are also divisible by 400 (so 2000 is a leap year, 1900 is not)"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def binary_search(items, target):
    """Index of target in the sorted list items, or -1 if target is not in the list"""
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

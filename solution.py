# Exercise 14 — Writing Your Own Tests
# These functions are already implemented correctly.
# Your job: write tests for them in test_solution.py.


def clamp(value, minimum, maximum):
    """Return value, but clamped between minimum and maximum.
    If value < minimum, return minimum.
    If value > maximum, return maximum.
    Otherwise return value.
    """
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def title_case(text):
    """Capitalise the first letter of each word, lowercase the rest."""
    return " ".join(word.capitalize() for word in text.split())


def is_anagram(a, b):
    """Return True if a and b are anagrams of each other.
    Ignore spaces and capitalisation.
    """
    clean = lambda s: sorted(s.replace(" ", "").lower())
    return clean(a) == clean(b)


def chunk(lst, size):
    """Split a list into chunks of the given size.
    The last chunk may be smaller.
    Example: chunk([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]
    """
    return [lst[i:i+size] for i in range(0, len(lst), size)]


def running_total(numbers):
    """Return a list of running totals.
    Example: running_total([1, 2, 3, 4]) -> [1, 3, 6, 10]
    """
    result = []
    total = 0
    for n in numbers:
        total += n
        result.append(total)
    return result

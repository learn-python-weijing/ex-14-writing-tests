# Exercise 14 — Writing Your Own Tests

## What you'll learn
- How to write `pytest` tests from scratch
- Thinking about **edge cases**
- The difference between a test that passes and a test that actually proves something

## Your task

This exercise is **different** — the functions are already implemented in `solution.py` and they work correctly.

**Your job is to write the tests in `test_solution.py`.**

## How to run the tests

```bash
pytest
```

All your tests should pass (since the functions are correct). If a test fails, your test is wrong — not the function.

## What makes a good test?

- Tests the **normal case** (typical input → expected output)
- Tests **edge cases** (empty input, zero, negative numbers, single items)
- Tests **boundary values** (the exact edges of valid ranges)
- Has a **clear name** that describes what it's testing

## Structure of a pytest test

```python
def test_something_specific():
    result = my_function(input)
    assert result == expected_output

def test_raises_error_when_invalid():
    import pytest
    with pytest.raises(ValueError):
        my_function(bad_input)
```

## Your goal

Write **at least 3 tests per function**. Think about what could go wrong and test for it.

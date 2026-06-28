# Discount Calculator

A simple Python function that calculates the final price after applying a discount, with input validation.

## What it does

`apply_discount(price, discount)` checks that the inputs are valid, then returns the final price after the discount is applied.

**Validation rules:**
- `price` and `discount` must be numbers (`int` or `float`).
- `price` must be greater than `0`.
- `discount` must be between `0` and `100`.

If any rule is broken, the function returns an error message instead of a number.

## Usage

```python
from discount import apply_discount

print(apply_discount(100, 20))   # 80.0
print(apply_discount(0, 20))     # "The price should be greater than 0"
print(apply_discount(100, 150))  # "The discount should be between 0 and 100"
```

## Requirements

- Python 3.6+
- No external dependencies
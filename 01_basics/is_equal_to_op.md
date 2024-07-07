### Understanding `==` and `is` in Python: A Code Example

In this example, we will explore the difference between the `==` operator and the `is` operator in Python, and how they relate to list references.

#### Code Snippet

```python
n = [1, 2, 3]
m = n
print(m)  # Output: [1, 2, 3]
print(n)  # Output: [1, 2, 3]
print(m == n)  # Output: True
print(m is n)  # Output: True

m = [1, 2, 3]
print(m)  # Output: [1, 2, 3]
print(m == n)  # Output: True
print(m is n)  # Output: False
```

**Explanation**:

1. **Initial Assignment**:
   ```python
   n = [1, 2, 3]
   m = n
   ```
   - `n` is assigned the list `[1, 2, 3]`.
   - `m` is assigned the same reference as `n`, so both `n` and `m` point to the same list.

2. **Comparisons**:
   ```python
   print(m == n)  # Output: True
   print(m is n)  # Output: True
   ```
   - `m == n` evaluates to `True` because the `==` operator checks for value equality, and `m` and `n` have the same contents.
   - `m is n` evaluates to `True` because the `is` operator checks for identity, meaning it checks if `m` and `n` refer to the exact same object in memory, which they do.

3. **Reassigning `m`**:
   ```python
   m = [1, 2, 3]
   print(m == n)  # Output: True
   print(m is n)  # Output: False
   ```
   - `m` is reassigned to a new list `[1, 2, 3]`. This new list is a different object in memory from the original list referenced by `n`.
   - `m == n` still evaluates to `True` because the contents of the new list `[1, 2, 3]` are the same as the contents of `n`.
   - `m is n` evaluates to `False` because `m` now references a new, separate list object, whereas `n` references the original list.

### Key Takeaways

- **`==` Operator**: This operator checks for value equality. It returns `True` if the values of the two objects are the same, regardless of whether they are the same object in memory.
- **`is` Operator**: This operator checks for identity. It returns `True` if the two references point to the exact same object in memory.

Understanding the difference between `==` and `is` is crucial in Python for correctly comparing objects, especially mutable objects like lists. Using `==` allows you to compare values, while `is` allows you to check if two references are to the same object.
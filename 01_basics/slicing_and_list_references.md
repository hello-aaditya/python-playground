### Understanding Slicing and List References in Python

In this code snippet, we will explore how slicing affects list references and mutability in Python.

#### Code Snippet

```python
h1 = [1, 2, 3]
h2 = h1[:]
print(h1)  # Output: [1, 2, 3]
print(h2)  # Output: [1, 2, 3]

h1[0] = 55
print(h1)  # Output: [55, 2, 3]
print(h2)  # Output: [1, 2, 3]
```

**Explanation**:
1. `h1` is assigned the list `[1, 2, 3]`.
2. `h2` is created by slicing `h1` with `h1[:]`. This creates a new list that is a copy of `h1`. Now `h1` and `h2` are two different lists, although they initially contain the same elements.
3. Printing `h1` and `h2` shows `[1, 2, 3]` for both, as `h2` is a copy of `h1`.
4. Modifying `h1[0]` to `55` changes the first element of the list referenced by `h1`.
5. Printing `h1` shows `[55, 2, 3]` because it reflects the modification.
6. Printing `h2` shows `[1, 2, 3]` because `h2` is a separate copy and remains unchanged.

### Key Takeaways

- **Slicing to Copy**: Using slicing (`h1[:]`) creates a shallow copy of the list, resulting in a new list that is independent of the original.
- **Separate References**: After slicing, `h1` and `h2` reference different lists, so changes to `h1` do not affect `h2`, and vice versa.
- **Mutability**: While lists are mutable and changes to a list through one reference affect all references to that list, slicing to create a copy ensures that changes to the original list do not impact the copied list.

This behavior highlights the importance of understanding references and copying mechanisms in Python to avoid unintended side effects when modifying lists.

```markdown
# Reading Lines from a File in Python

To read lines from a file in Python, you can use the `readline()` method or the `next()` function. This document explains both methods.

## Using `readline()` Method

The `readline()` method reads one line at a time from the file.

### Example

```python
# Open the file in read mode
f = open('file_name.py')

# Read the first line
line1 = f.readline()
print(line1)

# Read the second line
line2 = f.readline()
print(line2)

# Read the third line
line3 = f.readline()
print(line3)

# Close the file
f.close()
```

### Explanation

- **First `readline()` Call**: Reads the first line of `file_name.py`.
- **Second `readline()` Call**: Reads the second line of `file_name.py`.
- **Third `readline()` Call**: Reads the third line of `file_name.py`.
- **Subsequent `readline()` Calls**: Continue to read each subsequent line in the file.

Each call to `readline()` advances the file pointer to the next line, so the next call will read the next line in the file. When the end of the file is reached, `readline()` will return an empty string (`''`).

## Using `next()` Function

When you use the `next()` function, it is calling the `__next__()` method of the file iterator internally. Each call to `next(f)` reads the next line from the file.

### Example

```python
# Open the file in read mode
f = open('file_name.py')

# Use the next() function to read the first line
print(next(f))

# Use the next() function to read the second line
print(next(f))

# Use the next() function to read the third line
print(next(f))

# Close the file
f.close()
```

### Important Note

Using `next()` or `__next__()` directly will raise a `StopIteration` exception when the end of the file is reached.


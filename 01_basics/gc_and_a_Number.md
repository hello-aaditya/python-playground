# Question : How does Python's garbage collector handle a number?
Consider the following code:\

x = 12\
x = 5

Explain what happens to the number 12 in this scenario.
## Answer: 
In Python, memory management, including the handling of numbers, is managed by a system called the garbage collector. The garbage collector is responsible for automatically freeing up memory when objects are no longer needed.

Here's what happens step-by-step in your example:

    Initial Assignment:

    python

x = 12

    When you assign x = 12, the integer object 12 is created in memory, and x is a reference to this integer object.

Reassigning x:

python

    x = 5

        When you reassign x to 5, a new integer object 5 is created in memory (if it doesn't already exist), and x is updated to reference this new integer object 5.
        The reference count for the integer object 12 is decremented by 1 because x no longer refers to it.

What Happens to 12?

    Reference Counting: Python uses a reference counting mechanism as part of its memory management. Each object maintains a count of the number of references pointing to it. When the reference count drops to zero, it means there are no references to the object, and it can be safely deallocated.

    Garbage Collection:
        When x is reassigned from 12 to 5, the reference count for the integer object 12 is decremented.
        If there are no other references to the integer object 12, its reference count becomes zero.
        The garbage collector will then mark this object for deallocation, and its memory will be reclaimed in a future garbage collection cycle.
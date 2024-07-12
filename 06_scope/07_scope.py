#classic example of closure
def coffee_coder(num):
    def actual(x):
        return x ** num
    return actual

f = coffee_coder(2)
g = coffee_coder(3)

print(f(3))
print(g(3))
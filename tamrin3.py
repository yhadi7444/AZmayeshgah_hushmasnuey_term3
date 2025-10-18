




def f(w, x, y):
    n = len(x)
    return sum((y[i] - w * x[i])**2 for i in range(5, n))
x = [1, 5, 9, 17, 2, 4]
y = [22, 10, 45, 55, 2, 19]
w = 0.6

print(f(w, x, y))

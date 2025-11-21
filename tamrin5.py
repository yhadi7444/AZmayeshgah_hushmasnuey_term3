import math

w = float(input("w : "))
b = float(input("b : "))
a = float(input("a : "))
y = float(input("y : "))
for i in range(11):
    x = i / 10
    z = x * w + b
    a = math.log(1 + math.e ** z)
    w1 = -2 * (y - a) * math.e ** a + math.e ** a * x
    b1 = -2 * (y - a) * math.e ** a + math.e ** a * 1
    print("x =", x, " ln(1+e^z) =", a, " w1 =", w1, "b1 =", b1)
    #با کمک امیر صالحی
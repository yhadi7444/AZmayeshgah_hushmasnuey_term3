x = [1, 3]
y = [3, 7]
sum = 0
for i in range(2):
    sum += x[i] + y[i]
result1 = (sum* 2) / 100
print("جواب اولیه =", result1)
value1 = result1 * (x[0] + y[0])
value2 = result1 * (x[1] + y[1])
total = value1 + value2
final = total / 100
print("جواب =", final)
#با کمک صالحی
a = int(input())

b = []

for i in range(a):
  c = int(input())
  b.append(c)


check1 = b[1] - b[0]
check2 = b[1] // b[0]

if b[1] + check1 == b[2]:
  print(b[-1] + check1)
else:
  print(b[-1] * check2)
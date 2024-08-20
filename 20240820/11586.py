a = int(input())

b =[]

for i in range(a):
  b.append(input())

c = int(input())

if c == 1:
  for i in b:
    print(i)

elif c == 2:
  for i in b:
    change = list(i)
    change.reverse()
    result = ''.join(change)
    print(result)

elif c == 3:
  b.reverse()
  for i in b:
    print(i)
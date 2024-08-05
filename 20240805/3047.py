abc = []

a, b, c = map(int, input().split())
chk = input()

abc.append(a)
abc.append(b)
abc.append(c)
abc.sort()

for i in list(chk):
  if i == 'A':
    print(abc[0])
  elif i == 'B':
    print(abc[1])
  elif i == 'C':
    print(abc[2])
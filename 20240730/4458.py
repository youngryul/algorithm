n = int(input())

for i in range(n):
  a = list(input())
  a[0] = a[0].upper()
  print(''.join(a))
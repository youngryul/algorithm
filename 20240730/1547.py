n = int(input())

cup = [1, 2, 3]
for i in range(n):
  a, b = map(int, input().split())
  c = cup.index(a)
  d = cup.index(b)
  cup[c], cup[d] = cup[d], cup[c]

print(cup[0])
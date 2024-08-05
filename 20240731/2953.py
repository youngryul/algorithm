cook = [0,0,0,0,0]

for i in range(5):
  a, b, c, d = map(int, input().split())
  cook[i] = a+b+c+d

print(cook.index(max(cook))+1, max(cook))
a, b, c = map(int, input().split())

n = int(input())

result = []
cnt = 0


for i in range(3*n):
  a2, b2, c2 = map(int, input().split())

  if (i+1) % 3 != 0:
    cnt = cnt + (a*a2) + (b*b2) + (c*c2)
  else:
    cnt = cnt + (a*a2) + (b*b2) + (c*c2)
    result.append(cnt)
    cnt = 0

print(max(result))
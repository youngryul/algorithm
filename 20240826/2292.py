n = int(input())


cnt = 1

while n > 0:
  if n == 1 :
    break
  else:
    n = n - (6 * cnt)
    cnt = cnt + 1

print(cnt)
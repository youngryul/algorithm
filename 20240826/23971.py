h, w, n, m = map(int, input().split())

cnt1 = 0
cnt2 = 0

while h > 0:
  h = h - n -1
  cnt1 = cnt1 + 1

while w > 0:
  w = w - m - 1
  cnt2 = cnt2 + 1

print(cnt1 * cnt2)
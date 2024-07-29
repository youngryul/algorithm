a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

# 만 나이 계산 : 기준 연도에서 생년을 뺀 뒤 생일 지나지 않았으면 -1 생일이거나 생일이 지났으면 0
year = d - a
if e < b:
  year -= 1
elif e == b and f < c:
  year -= 1

print(year)
print(d-a+1)
print(d-a)
  
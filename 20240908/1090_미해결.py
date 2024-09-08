import statistics 

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

x = []
y = []
x_chk = 0 
y_chk = 0

for i in arr:
  x.append(i[0])
  y.append(i[1])

result = []

for i in range(n):
  x_md = statistics.median(x[0:i+1])
  y_md = statistics.median(y[0:i+1])
  result.append(abs(x[i]-x_md) + abs(y[i] - y_md))

print(result)

# 중앙값을 구해서 다 더해주는 로직 ? 
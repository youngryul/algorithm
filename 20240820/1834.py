n = int(input())

result = 0

for i in range(n-1):
  result = result + n * (i+1) + (i+1)

print(result)
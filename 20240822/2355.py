a, b = map(int, input().split())

result = 0 

sigma = []
sigma.append(a)
sigma.append(b)
sigma.sort()

a = sigma[0]
b = sigma[1]

result = ((a+b) * (b-a+1) // 2)

print(result)
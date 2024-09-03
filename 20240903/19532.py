a, b, c, d, e, f = map(int, input().split())

x = (c*e - b*f) // (a*e - d*b)
y = (c*d - a*f) // (d*b - a*e)

print(x,y)

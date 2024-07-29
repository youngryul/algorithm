a = int(input())
b, c = map(int, input().split()) 

cnt = 0 

cnt = b//2 + c

if cnt > a:
  cnt = a

print(cnt)
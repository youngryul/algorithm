n = int(input())

for _ in range(n): # 단순 반복일때는 변수가 필요없으니까_처리 
  number = int(input())

  for i in range(2,1_000_001):
    if number % i == 0:
      print("NO")
      break
    if i == 1_000_000:
      print("YES")
      
  
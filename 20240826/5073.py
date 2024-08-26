while True:
  a, b, c = map(int, input().split())

  lst = []
  lst.append(a)
  lst.append(b)
  lst.append(c)
  lst.sort()
  
  if a == 0 and b == 0 and c == 0:
    break
  else:
    if lst[2] >= (lst[0]+lst[1]):
      print("Invalid")
    elif a == b == c:
      print("Equilateral")
    elif a == b or b == c or a == c:
      print("Isosceles")
    else:
      print("Scalene")
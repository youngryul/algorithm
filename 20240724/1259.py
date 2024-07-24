while True:
  a = int(input())

  if a == 0:
    break
  else:
    ## 알고리즘 문제
    a_list = list(map(int,str(a)))
    a_reverse = list(map(int, str(a)))
    a_reverse.reverse()
    if a_list == a_reverse:
      print("yes")
    else:
      print("no")
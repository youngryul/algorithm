while True:
  a = list(map(str, input().split()))
  cnt = 0

  if a[0] == '#':
    break
  else:
    for i in a:
      for j in list(i):
        if a[0] == j.lower():
          cnt = cnt + 1

    print(a[0], cnt-1)
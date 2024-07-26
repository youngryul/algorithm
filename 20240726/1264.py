while True:
  a = input()

  if a == '#':
    break
  else:
    # 코드입력
    vowels = ['a', 'i', 'o', 'u', 'e']
    cnt = 0

    for i in vowels:
      for j in a:
        if i.lower() == j.lower():
          cnt += 1

    print(cnt)
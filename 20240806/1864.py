while True:
  a = input()

  if a == '#':
    break
  else:
    ten = {
      "-": 0,
      "\\": 1,
      "(": 2,
      "@": 3,
      "?": 4,
      ">": 5,
      "&": 6,
      "%": 7,
      "/": -1
    }

    cnt = len(list(a)) - 1


    result = 0
    
    for i in list(a):
      result = ten[i] * (8 ** cnt) + result
      cnt = cnt - 1

    print(result)      
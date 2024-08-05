cnt = []

for i in range(5):
  a = input()
  if "FBI" in a:
    cnt.append(i+1)

if len(cnt) == 0:
  cnt.append('HE GOT AWAY!')

for i in cnt:
  print(i)
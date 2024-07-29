a = input()

vowels = ['a', 'i', 'o', 'u', 'e']
cnt = 0

for i in vowels:
  for j in a:
    if i == j:
      cnt += 1

print(cnt)
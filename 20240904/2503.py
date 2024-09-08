n = int(input())

hint = [list(map(str, input().split())) for _ in range(n)] #리스트 for문 돌리기

answer = 0 

for a in range(1,10):
  for b in range(1,10):
    for c in range(1,10):

      if ( a==b or b==c or c==a):
        continue
        
      count = 0
      for arr in hint : 
        num = list(arr[0]) #자릿수로 비교해야하기 때문에 
        strike = int(arr[1])
        ball = int(arr[2])


        strike_count = 0 #숫자들 중 하나가 세자리 수의 동일한 자리에 위치하면 스트라이크 한번 
        ball_count = 0 #숫자가 세 자리 수에 있긴 하나 다른 위치에 위치하면 볼 한번 


        if (int(num[0]) == a) :
          strike_count +=1 
        if (int(num[1]) == b) :
          strike_count +=1 
        if (int(num[2]) == c) :
          strike_count +=1

        if (int(num[0]) == b) or (int(num[0]) == c) :
          ball_count+=1

        if (int(num[1]) == a) or (int(num[1]) == c) :
          ball_count+=1

        if (int(num[2]) == a) or (int(num[2]) == b) :
          ball_count+=1

        if strike_count == strike and ball_count == ball :
          count += 1 
        else:
          break

               
      if count == n :
        answer += 1 
           


print(answer)
                   
            
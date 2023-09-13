# 1~15까지 출력
for i in range(15) :
    print(i)

# 30~1까지 출력
for i in range(30) :
    print(30-i)
# 1~100까지 중 홀수만 출력
for i in range(50) :
    print((i*2)+1)
# 1~10까지 합 출력
total1 = 0
for i in range(10):
    total1+=i+1
print(f"total2 : {total1}")
# 1~n까지 합 출력
total2 = 0
for i in range(int(input("1~n까지 합 n :"))) :
    total2+=(i+1)
print(f"total2 : {total2}")

# 3 4 5 6 3 4 5 6 3 4 5 6 출력
for i in range(12) :
    print((i%4)+3)




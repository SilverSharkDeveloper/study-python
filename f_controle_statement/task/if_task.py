message = f"원하시는 색깔을 영어로 바꿔드립니다!\n1.빨간색\n2.검은색\n3.노란색\n4.흰색\n 번호 :"


choice = int(input(message))

color = ""

if choice ==1 :
    color ="red"
elif choice ==2 :
    color="black"
elif choice ==3 :
    color="yellow"
else:
    color="white"

print(f"당신이 고른 색깔은 영어로 {color}입니다")
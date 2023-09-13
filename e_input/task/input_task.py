# email을 입력받고 아이디( email_id)와 도메인(domain)을 각각 변수에 담고 출력
#첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서 각각 cm로 변환하여 다음 형식에 맞추어
#소수점 둘 째짜리 까지 출력한다.

#yard : 10
#inch : 10

#1yard = 91.44cm
#1inch = 2.54cm


email,domain = input("이메일을 입력해주세요 : ").split("@")


domain = domain.replace(".com","")

print(f"당신의 이메일은 : {email} , 도메인은 {domain} 입니다")


yard_inch = input("yard 와 inch를 입력 (공백): ").split(" ")

yard = int(yard_inch[0]);
inch = int(yard_inch[1]);

print("입력한 yard는 약%.2fcm 이고 inch는 약 %.2fcm입니다" %(yard*91.44,inch*2.54))

# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의

class Taxi :
    base_fee = 5800
    base_distance = 2

    def __init__(self,name):
        self.name = name




    def need_money(self,passenger_name,distance):
        if distance>Taxi.base_distance :
            print(f"{passenger_name}님 내실 금액은{Taxi.base_fee + (distance-Taxi.base_distance)*1000}입니다")
            return Taxi.base_fee + (distance-Taxi.base_distance)*1000
        else:
            print(f"{passenger_name}님내실 금액은 {Taxi.base_fee}")
            return Taxi.base_fee

    def change_money(self,passenger_name,money,distance):
        change = money-self.need_money(passenger_name,distance)

        print(f"{passenger_name}님 잔돈은{change}")
        return change


taxi1 = Taxi("택시1")
taxi2 = Taxi("택시2")



taxi1.change_money("허은상",6000,2)


# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의
class Taxi:
    init_fare = 5800
    init_distance = 2
    fare_per_km = 1000

    def __init__(self, money, distance):
        self.money = money
        self.distance = distance

    def calc_cost(self):
        cost = Taxi.init_fare
        if self.distance > Taxi.init_distance:
            cost += (self.distance - Taxi.init_distance) * Taxi.fare_per_km

        return cost

    def get_change(self):
        change = self.money - self.calc_cost()
        return change


passenger1 = Taxi(20000, 1)
passenger2 = Taxi(30000, 10)

print(passenger1.calc_cost(), passenger1.get_change())
print(passenger2.calc_cost(), passenger2.get_change())


















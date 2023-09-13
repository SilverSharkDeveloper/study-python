# 동물
# 이름,나이,성별
#먹기 : 음식 1개 소진
#산책하기 : 음식 1개 획득, 체력 1개소진



class Animal:
    total_food = 10
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.food_count = 0
        self.health = 10


    def __str__(self):
        return f"{self.name} : 음식갯수 : {self.food_count}, 체력 :{self.health}"


    def eat(self,food):
        if Animal.total_food==0:
                print(f"남아있는 음식이 없습니다.")
        elif self.food_count>0 :
            print(f"{self.name}이 {food}를 먹습니다.")
            self.food_count -= 1
        else :
            print(f"먹을 수 있는 음식이 없습니다. 산책부터하세요")

        print(self)

    def run(self):
        print(f"{self.name}이 산책을 나갑니다.")
        if Animal.total_food>0 :
            Animal.total_food -= 1
            self.food_count += 1
            print(f"음식을 획득합니다.")
        else:
            print("힘겹게 산책했지만 음식은 없습니다.")

        self.health-=1
        print(self)


dog = Animal("개",14,"M")
cat = Animal("고양이",13,"W")
pig = Animal("돼지",178,"M")


dog.eat("개껌")
dog.run()
dog.eat("개껌")

print(Animal.total_food)
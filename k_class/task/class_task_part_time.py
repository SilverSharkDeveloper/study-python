# PartTimer

# '모든 직원'에 공통적으로 적용되는 내용
# - 시급
# - 직원수

# '각 직원'별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(초기값: 0, 생성자로 초기화 불가능)

# 직원 급여 계산
#   '근무 시간 + 상여금'에 따른 직원 급여 계산
#   '상여금'은 지정 하지 않으면 0 으로 처리


class PartTimer :
    hourly_wage = 1000
    total_Part_timer = 0

    def __init__(self,nickname,work_place='청담동'):
        self.nickname= nickname
        self.work_space = work_place
        self.total_salary = 0
        PartTimer.total_Part_timer+=1

    def get_totla_salary(self,working_time,bonus=0):
        self.total_salary = working_time * PartTimer.hourly_wage + bonus
        return self.total_salary



a = PartTimer("a")
b = PartTimer("b")
c = PartTimer("c")
d = PartTimer("d")


print(a.get_totla_salary(5,1000))
print(b.get_totla_salary(10))

print(PartTimer.total_Part_timer)

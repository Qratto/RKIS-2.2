class FitnessCenter():
    def __init__(self,code,year,month,duration):
        self.code = code
        self.year = year
        self.month = month
        self.duration = duration

list = [
    FitnessCenter(1,2007,7,90),
    FitnessCenter(2,2022,3,30),
    FitnessCenter(3,2014,4,100),
    FitnessCenter(4,2005,12,60),
    FitnessCenter(5,2011,8,80)
]

short = list[0]
long = list[0]

for i in list:
    if i.duration < short.duration:
        short = i
        continue
    if i.duration > long.duration:
        long = i

print(f"Самое продолжительное занятие код: {long.code} год: {long.year} " 
      f"месяц: {long.month} продолжительность: {long.duration} минут ")

print(f"Самое короткое занятие код: {short.code} год: {short.year} " 
      f"месяц: {short.month} продолжительность: {short.duration} минут ")
class FitnessCenter():
    def __init__(self,code,year,month,duration):
        self.code = code
        self.year = year
        self.month = month
        self.duration = duration

list = [
    FitnessCenter(1,2022,7,90),
    FitnessCenter(2,2022,3,30),
    FitnessCenter(3,2014,4,100),
    FitnessCenter(4,2005,12,60),
    FitnessCenter(5,2011,8,80),
    FitnessCenter(6,2007,7,90),
    FitnessCenter(7,2023,3,30),
    FitnessCenter(8,2014,4,10),
    FitnessCenter(9,2010,12,60),
    FitnessCenter(10,2023,8,80)
]

total = {}
total_duration = 0
black_list = []
for i in list:
    year_check = i.year
    #Проверка на повторение годов
    if not year_check in black_list:
        total_duration = 0
        black_list.append(year_check)
        #Суммирование продолжительности за определённый год
        for j in list:
            if year_check == j.year:
                total_duration += j.duration
        total[i.year] = total_duration    

max_duration = max(total.values())

best_years = []

for year, total in total.items():
    if total == max_duration:
        best_years.append(year)

best_year = min(best_years)

print(f"Год: {best_year} суммарная продолжительность: {max_duration}")


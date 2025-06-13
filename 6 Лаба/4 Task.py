numbers = [-1, -2, 4,-5,1,2,3,]

for i in range(len(numbers)):
    if numbers[i] > 0:
        print("Первый положительный элемент:",numbers[i])
        break

for i in range(len(numbers)-1,-1,-1):
    if numbers[i] < 0:
        print("Последний отрицательный элемент:",numbers[i])
        break
    
array = []

for i in range(14):
    try:
        num = int(input())
        array.append(num)
    except ValueError:
        print("Введено не правильное значение")

array.append(sum(array))

for i in array:
    print(i,end=" ")
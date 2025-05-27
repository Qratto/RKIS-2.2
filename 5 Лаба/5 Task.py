def calculating_expression(num_one,num_two):
    return (num_one + 4 * num_two)*(num_one - 3 * num_two) + num_one * 2


num_a = int(input("Введите число a: "))
num_b = int(input("Введите число b: "))

result = calculating_expression(num_a,num_b)
print(result)
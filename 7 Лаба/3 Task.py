numbers = [2,-14,15,-1,3,10,-12]

two_digit_numbers = []

for number in numbers:
    if (number // 10) != 0 and number > 0:
        two_digit_numbers.append(number)

print(two_digit_numbers)



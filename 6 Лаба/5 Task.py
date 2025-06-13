line = "hi mom i was born"
symbol = 'm'
line_list = []

count = 0

line_list.extend(line.split())
for word in line_list:
    if len(word) > 1 and word[0] == symbol and word[-1] == symbol:
        count += 1

print("Кол-во элементов:",count)

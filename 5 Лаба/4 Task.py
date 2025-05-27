line = input("Введите строку: ")
if line[:3] == "abc":
    line = "www" + line[3:]
    print(line)
else:
    line = line + "zzz"

print(line)

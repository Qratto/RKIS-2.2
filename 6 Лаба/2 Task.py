class User():
    def __init__(self,login: str, password: str):
        self.login = login
        self.password = password

login_input = input("Введите логин: ")

users = [
    User("overgo","}=T[x&$V"),
    User("rodmen","Km4#kGhu"),
    User("uniter","1fW/C_1F"),
    User("firers","JRyGkm>3"),
    User("nivose","I/zLtmB-")
]

for user in users:
    if user.login == login_input:
        print(f"Логин: {user.login}, пароль: {user.password}")
print("Добро пожаловать в игру!")
username = input("Пожалуйста, представьтесь: ")
print("Вам надо отгадать слова")

answer = "ТОКИО"

word = []

for i in range(len(answer)):
    word.append('*')

print(*word)

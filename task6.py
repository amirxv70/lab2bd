s = input("Введите строку: ")
vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"
count = 0

for c in s:
    if c in vowels:
        count += 1

print("Количество гласных:", count)

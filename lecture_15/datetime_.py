from datetime import date

today = date(2023,10,17)

print(today)

print(type(today))

birthday = date(1997,2,16)

print(today - birthday)

print(birthday.strftime("%A, %B, %d"))

name = "Chao Jiang"

print(name.upper())

print(name.lower())

print(name.swapcase())

print(name.isdigit())
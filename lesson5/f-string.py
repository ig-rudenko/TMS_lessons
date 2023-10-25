name = input("Ваше имя: ")
age = int(input("Ваш возраст: "))

text = f"""
==================
  Ваш профиль:
  Имя:     {name.title()}
  Возраст: {age+1}
  Number:  {2/6:.2}
==================
"""

print(text)


text = f"Привет, {name.title() + ''}"
print(text)

a = "12.31"
b = "100.00"
c = "3.93"

text = f"""
{a:>5} | {b:>5} | 
{c:>5} | {a:>5} | 
{b:>5} | {c:>5} | 
"""
print(text)

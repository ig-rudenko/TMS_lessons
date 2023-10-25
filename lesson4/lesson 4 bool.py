# BOOLEAN, bool, булево значение

a = 1
b = 0

boolean = (a < b)
# Числа?
# False или 0
# True или 1

print(boolean)

print(boolean + 2)

print("=========== todo ===========")

# Порог, при котором вы знаете python
PYTHON_LEVEL = 0.871287391823916237861  # Константа

python_score = 0.9
todo = [
    {
        "name": "Выучить python",
        "status": False,
    },
    {
        "name": "Выучить C++",
        "status": True,
    },
]

status = (python_score > PYTHON_LEVEL)  # True
todo[0]["status"] = status


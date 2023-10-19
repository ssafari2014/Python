# ماشین حساب
from replit import clear
from logo import logo

# تابع جمع

def add(n1, n2):
    """دو عدد را با هم جمع می کند """
    return n1 + n2


# تابع تفریق
def subtraction(n1, n2):
    """دو عدد را با هم تفریق می کند """
    return n1 - n2


# تابع ضرب
def multiplication(n1, n2):
    """دو عدد را با هم ضرب می کند """
    return n1 * n2


# تابع تقسیم
def Division(n1, n2):
    """دو عدد را با هم تقسیم  می کند """
    return n1 / n2


# تابع باقیمانده
def left_over(n1, n2):
    """باقیمانده دو عدد را بر میگرداند """
    return n1 % n2


operators = {
    '+': add,
    '-': subtraction,
    '*': multiplication,
    '/': Division,
    '%': left_over,
}


# x = operators['-']
# print(x(2,3))

# عدد اول را از کارربر دریاقت میکنیم
def calculator():
    print(logo)
    num1 = int(input('Enter the first number: '))
    for item in operators:
        print(item)
    Continue_calculation = True
    while Continue_calculation:
        operations_symbol = input('Pick an operation ?')
        num2 = int(input('Enter the next number: '))
        calculation_functions = operators[operations_symbol]
        answer = calculation_functions(num1, num2)

        print(f'{num1} {operations_symbol} {num2} = {answer}')

        if input(f"type 'y' to Continue calculation with : {answer} or type 'n' to exit :") == "Y":
            num1 = answer
        else:
            Continue_calculation = False
            calculator()
calculator()
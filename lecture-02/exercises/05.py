#
from decimal import Decimal, getcontext

getcontext().prec = 10
def complex_interest(P, r, n, t):
    principal = Decimal(P)
    rate = Decimal(r) / Decimal(100)
    times_compounded = Decimal(n)
    years = Decimal(t)

    A = principal * (1 + (rate / times_compounded)) ** (times_compounded * years)
    return A

first_amount = int(input("Введите сумму вклада: "))
annual_rate = int(input("Введите процентную ставку за год: "))
compounds_per_year = int(input("Количество капитализаций за год: "))
investment_years = int(input("Срок вклада: "))

result = complex_interest(first_amount, annual_rate, compounds_per_year, investment_years)
print(f"Загальна сума вкладу з урахуванням складних відсотків: {result}")

#
from decimal import Decimal, getcontext
getcontext().prec = 17
def calculate_emi(Princiapl_amount_borrowed, Periodic_monthly_interest_rate, Total_number_of_monthly_payments):
    P = Decimal(Princiapl_amount_borrowed)
    r = Decimal(Periodic_monthly_interest_rate) / Decimal(12 * 100)
    n = Decimal(Total_number_of_monthly_payments)

    emi = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return emi

principal_amount = 500000 
annual_rate = 8
total_months = 24

emi = calculate_emi(principal_amount, annual_rate, total_months) 
print(f"Вихідні дані: EMI for {total_months} months: {emi}")

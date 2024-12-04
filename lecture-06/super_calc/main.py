from super_calc.operations import ops
from super_calc.menu import menu, calc_help

def extract(entry):
    for o in ops.keys():
        if o in entry:
            parts = entry.split(o)
            if len(parts) == 2:
                a, b = parts
                return a.strip(), b.strip(), o
    return None, None, None

def result(a, b, operator):
    try:
        a, b = float(a), float(b)
        if operator == '/' and b == 0:
            return None, "Oops, division by zero"
        elif operator in ('//', '%') and b == 0:
            return None, "Oops, division or modulo by zero"
        else:
            return ops[operator](a, b), ''
    except ValueError:
        return None, "Invalid input. Please enter numeric values."

while True:
    choice = menu()

    if choice == 'q':
        print('Thank you for using Super Calc!')
        break
    
    if choice == 'h':
        calc_help()
        continue

    if choice == 'c':
        entry = input("Enter x operator y (e.g., 2 + 2): ")
        a, b, operator = extract(entry)
        
        if not operator:
            calc_help("Invalid format or unsupported operator.")
            continue
        
        res, err = result(a, b, operator)
        if err:
            print(err)
        else:
            print(f"{a} {operator} {b} = {res}")

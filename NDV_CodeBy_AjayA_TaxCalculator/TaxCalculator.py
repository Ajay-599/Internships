def calculate_taxes():
    ctc = float(input("Enter your Total CTC: "))
    bonus = float(input("Enter your Bonus Amount: "))

    total_income = ctc + bonus
    print(f"Total Income: {total_income:.2f}")

    old_taxable_income = max(0, total_income - 220000)
    old_tax = calculate_old_tax(old_taxable_income)

    new_tax = calculate_new_tax(total_income)

    print(f"Old Regime Tax: {old_tax:.2f}")
    print(f"New Regime Tax: {new_tax:.2f}")

def calculate_old_tax(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    else:
        return 12500 + (income - 500000) * 0.2

def calculate_new_tax(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    elif income <= 1000000:
        return 12500 + (income - 500000) * 0.2
    else:
        return 112500 + (income - 1000000) * 0.3

calculate_taxes()

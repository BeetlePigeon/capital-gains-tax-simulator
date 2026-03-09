import math

standard_deduction = 15750
brackets = [
    [0, 11925, .1],
    [11925, 48475, .12],
    [48475, 103350, .22],
    [103350, 197300, .24],
    [197300, 250525, .32],
    [250525, 626350, .35],
    [626350, math.inf, .37],
]

long_brackets = [
    [0, 48475, 0],
    [48475, 492300, .15],
    [492300, math.inf, .2]
]

def federal_taxes(gross_income):
    taxable_income = max(0, gross_income - standard_deduction)
    federal_tax = 0
    for index, bracket in enumerate(brackets):
        federal_tax += max(min(taxable_income, brackets[index][1]) - brackets[index][0], 0) * brackets[index][2]
    return federal_tax

def long_taxes(gross_income, long_income):
    taxable_income = max(0, gross_income - standard_deduction) + long_income
    long_tax = 0
    for index, bracket in enumerate(long_brackets):
        long_tax += max(min(taxable_income, long_brackets[index][1]) - long_brackets[index][0], 0) * long_brackets[index][2]
    return long_tax

def get_tax_info(salary):
    print(f'If salary: ${salary:,}, LTCG: ${long_gains:,}, STCG: ${short_gains:,} then:')
    print(f'Federal taxes owed: ${federal_taxes(salary):,.2f}')
    print(f'Profit with no STCG/LTCG: ${salary-federal_taxes(salary):,.2f}')

    print(f'LTCG taxes owed: ${federal_taxes(salary)+long_taxes(salary, long_gains):,.2f}')
    print(f'Profit with LTCG: ${salary+long_gains-(federal_taxes(salary)+long_taxes(salary, long_gains)):,.2f}')

    print(f'STCG taxes owed: ${federal_taxes(salary+short_gains):,.2f}')
    print(f'Profit with STCG: ${salary+short_gains-federal_taxes(salary+short_gains):,.2f}')

if __name__ == '__main__':
    my_salary = 60000
    long_gains = 150000
    short_gains = 170000
    get_tax_info(my_salary)
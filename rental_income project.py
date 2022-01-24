"""
1. I used class variables and therefore needed to use the class name
througout each of the methods. This seems cluttered; I'm not sure how to get around this.

2. I decided against the 'input' function because it just seems silly if these
programs aren't going to be used front-end. Maybe there's somtehing I don't understand but.
I guess a nice GUI would be the best option, but I wouldn't know where to start.

3. A test instance is written below so you can just run this bish as an example.

"""

class RentalProp:
    #class variables generated from methods
    income = 0 
    expenses = 0
    cashflow = 0
    investment = 0
    roi=0

    def __init__(self, address, city):
        self.address = address
        self.city = city

    def income_calc(self, rental_income,other_income):
        RentalProp.income = rental_income + other_income
        return(f"This property should make ${RentalProp.income} per month.")

    def expenses_calc(self, tax, insurance, utilities, prop_management, vacancy, other):
        RentalProp.expenses = tax + insurance + utilities + prop_management + vacancy + other
        return(f"This property should cost ${RentalProp.expenses} per month.")

    def investment_calc(self, down_payment, closing_costs, rehab_budget):
        RentalProp.investment = down_payment + closing_costs + rehab_budget
        return(f"Your total property investment is ${RentalProp.investment} per month.")

    def roi_calc(self):
        RentalProp.cashflow = RentalProp.income - RentalProp.expenses
        RentalProp.roi = round((RentalProp.cashflow/RentalProp.investment * 100),2)
        roi_adj = ""
        if RentalProp.roi < 1:
            roi_adj="horrible & atrocious"
        elif 1 <= RentalProp.roi < 3:
            roi_adj = "pretty bad"
        elif 3 <= RentalProp.roi < 5:
            roi_adj = "acceptable"
        elif 5 <= RentalProp.roi < 10:
            roi_adj = "reasonable"
        elif 10 <= RentalProp.roi:
            roi_adj = "pretty great"

        print(f"Your ROI is {RentalProp.roi}%. This is a {roi_adj} return.")

first_house = RentalProp("100 Birch Ln Ct Dr", "Odessa")
print(first_house.city)
first_house.income_calc(1000,500)
print(first_house.income)
first_house.expenses_calc(100,200,300,200,100,300)
print(first_house.expenses)
first_house.investment_calc(30000,5000,20000)
print(first_house.investment)
first_house.roi_calc()
print(first_house.roi)








